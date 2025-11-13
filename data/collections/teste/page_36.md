[Skip to main content](https://ohmyposh.dev/docs/segments/cli/nix-shell#__docusaurus_skipToContent_fallback)

If you're enjoying Oh My Posh, consider becoming a [sponsor](https://github.com/sponsors/JanDeDobbeleer) to keep the project going strong 💪

On this page

## What [​](https://ohmyposh.dev/docs/segments/cli/nix-shell\#what "Direct link to What")

Displays the [nix shell](https://nixos.org/guides/nix-pills/developing-with-nix-shell.html) status if inside a nix-shell environment.

## Sample Configuration [​](https://ohmyposh.dev/docs/segments/cli/nix-shell\#sample-configuration "Direct link to Sample Configuration")

- json
- yaml
- toml

```json
{
  "type": "nix-shell",
  "style": "powerline",
  "foreground": "blue",
  "background": "transparent",
  "template": "(nix-{{ .Type }})"
}
```

```yaml
type: nix-shell
style: powerline
foreground: blue
background: transparent
template: (nix-{{ .Type }})
```

```toml
type = "nix-shell"
style = "powerline"
foreground = "blue"
background = "transparent"
template = "(nix-{{ .Type }})"
```

## Template ( [info](https://ohmyposh.dev/docs/configuration/templates)) [​](https://ohmyposh.dev/docs/segments/cli/nix-shell\#template-info "Direct link to template-info")

default template

```template
via {{ .Type }}-shell"
```

### Properties [​](https://ohmyposh.dev/docs/segments/cli/nix-shell\#properties "Direct link to Properties")

| Name | Type | Description |
| --- | --- | --- |
| `.Type` | `string` | the type of nix shell, can be `pure`, `impure` or `unknown` |

- [What](https://ohmyposh.dev/docs/segments/cli/nix-shell#what)
- [Sample Configuration](https://ohmyposh.dev/docs/segments/cli/nix-shell#sample-configuration)
- [Template (info)](https://ohmyposh.dev/docs/segments/cli/nix-shell#template-info)
  - [Properties](https://ohmyposh.dev/docs/segments/cli/nix-shell#properties)