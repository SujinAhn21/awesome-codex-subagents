# MCP Exclusions

The default conversion build excludes these upstream agents because they explicitly depend on MCP or
MCP-style runtime surfaces.

## Excluded Agents

1. `ui-ux-tester`
   Source: `categories/04-quality-security/ui-ux-tester.md`
2. `mcp-developer`
   Source: `categories/06-developer-experience/mcp-developer.md`
3. `visual-asset-generator`
   Source: `categories/06-developer-experience/visual-asset-generator.md`
4. `healthcare-admin`
   Source: `categories/07-specialized-domains/healthcare-admin.md`
5. `codebase-orchestrator`
   Source: `categories/09-meta-orchestration/codebase-orchestrator.md`
6. `scientific-literature-researcher`
   Source: `categories/10-research-analysis/scientific-literature-researcher.md`

## Notes

- This exclusion set is driven by the current repository policy and current automated classification.
- `healthcare-admin` is excluded conservatively because its workflow references external MCP-like data
  integrations. It can be revisited later if you want a softer classification rule.
