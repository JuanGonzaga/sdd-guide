#!/usr/bin/env python3
"""
Parser do Jira issue JSON + ADF (Atlassian Document Format) → texto.

Uso:
    python3 parse_adf.py /tmp/jira-IMC-1222.json

Recebe o JSON retornado por GET /rest/api/3/issue/<KEY> e imprime os campos
relevantes já com descrição e comentários convertidos de ADF para texto plano.
"""
import json
import sys


def adf_to_text(node, depth=0):
    """Conversor mínimo de ADF para texto. Cobre os tipos mais comuns."""
    if node is None:
        return ""
    if isinstance(node, list):
        return "\n".join(adf_to_text(n, depth) for n in node)
    if not isinstance(node, dict):
        return str(node)

    t = node.get("type", "")
    content = node.get("content", [])

    if t == "text":
        return node.get("text", "")
    if t in ("paragraph", "heading"):
        return adf_to_text(content, depth) + "\n"
    if t == "bulletList":
        items = [
            "- " + adf_to_text(c.get("content", []), depth).strip()
            for c in content
        ]
        return "\n".join(items) + "\n"
    if t == "orderedList":
        items = [
            f"{i}. " + adf_to_text(c.get("content", []), depth).strip()
            for i, c in enumerate(content, 1)
        ]
        return "\n".join(items) + "\n"
    if t == "listItem":
        return adf_to_text(content, depth)
    if t == "codeBlock":
        return "```\n" + adf_to_text(content, depth) + "```\n"
    if t == "hardBreak":
        return "\n"
    if t == "mention":
        attrs = node.get("attrs", {})
        return "@" + attrs.get("text", attrs.get("displayName", ""))
    if t in ("inlineCard", "blockCard"):
        attrs = node.get("attrs", {})
        return attrs.get("url", "")
    if t == "rule":
        return "\n---\n"
    # fallback: descer recursivamente
    return adf_to_text(content, depth)


def main(path):
    with open(path) as f:
        data = json.load(f)

    fields = data.get("fields", {}) or {}

    def g(d, *keys):
        cur = d
        for k in keys:
            if cur is None:
                return None
            cur = cur.get(k) if isinstance(cur, dict) else None
        return cur

    print("=" * 70)
    print(f"KEY:      {data.get('key')}")
    print(f"SUMMARY:  {fields.get('summary')}")
    print(f"STATUS:   {g(fields, 'status', 'name')}")
    print(f"TYPE:     {g(fields, 'issuetype', 'name')}")
    print(f"PRIORITY: {g(fields, 'priority', 'name')}")
    print(f"ASSIGNEE: {g(fields, 'assignee', 'displayName')}")
    print(f"REPORTER: {g(fields, 'reporter', 'displayName')}")
    print(f"CREATED:  {fields.get('created')}")
    print(f"UPDATED:  {fields.get('updated')}")
    print(f"DUE:      {fields.get('duedate')}")
    print(f"LABELS:   {fields.get('labels')}")
    print(f"COMPONENTS:   {[c.get('name') for c in (fields.get('components') or [])]}")
    print(f"FIX VERSIONS: {[v.get('name') for v in (fields.get('fixVersions') or [])]}")

    parent = fields.get("parent")
    if parent:
        print(f"PARENT:   {parent.get('key')} - {g(parent, 'fields', 'summary')}")

    subs = fields.get("subtasks") or []
    if subs:
        print("SUBTASKS:")
        for s in subs:
            print(
                f"  - {s.get('key')}: {g(s, 'fields', 'summary')} "
                f"[{g(s, 'fields', 'status', 'name')}]"
            )

    links = fields.get("issuelinks") or []
    if links:
        print("LINKS:")
        for l in links:
            rel = g(l, "type", "outward") or g(l, "type", "inward")
            target = l.get("outwardIssue") or l.get("inwardIssue") or {}
            print(f"  - {rel}: {target.get('key')} - {g(target, 'fields', 'summary')}")

    print()
    print("=" * 70)
    print("DESCRIPTION:")
    print("=" * 70)
    print(adf_to_text(fields.get("description")) if fields.get("description") else "(vazio)")

    print()
    print("=" * 70)
    print("ATTACHMENTS:")
    print("=" * 70)
    atts = fields.get("attachment") or []
    if atts:
        for a in atts:
            print(f"  - {a.get('filename')} ({a.get('mimeType')}, {a.get('size')} bytes)")
    else:
        print("(nenhum)")

    print()
    print("=" * 70)
    print("COMMENTS:")
    print("=" * 70)
    cobj = fields.get("comment") or {}
    comments = cobj.get("comments") or []
    total = cobj.get("total")
    if total is not None and len(comments) < total:
        print(f"⚠ {len(comments)}/{total} comentários retornados — buscar restantes via /comment?startAt={len(comments)}")
        print()
    if comments:
        for c in comments:
            author = g(c, "author", "displayName")
            created = (c.get("created") or "")[:10]
            print(f"\n--- {author} @ {created} ---")
            print(adf_to_text(c.get("body")))
    else:
        print("(nenhum)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: parse_adf.py <jira-issue.json>", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
