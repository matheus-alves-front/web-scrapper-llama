[Skip to main content](https://ohmyposh.dev/docs/segments/cli/svelte#__docusaurus_skipToContent_fallback)

If you're enjoying Oh My Posh, consider becoming a [sponsor](https://github.com/sponsors/JanDeDobbeleer) to keep the project going strong 💪

On this page

## What [​](https://ohmyposh.dev/docs/segments/cli/svelte\#what "Direct link to What")

Display the currently active Svelte version.

## Sample Configuration [​](https://ohmyposh.dev/docs/segments/cli/svelte\#sample-configuration "Direct link to Sample Configuration")

- json
- yaml
- toml

```json
{
  "type": "svelte",
  "style": "powerline",
  "powerline_symbol": "",
  "foreground": "#000000",
  "background": "#1976d2",
  "template": "  {{ .Full }} "
}
```

```yaml
type: svelte
style: powerline
powerline_symbol: 
foreground: "#000000"
background: "#1976d2"
template: "  {{ .Full }} "
```

```toml
type = "svelte"
style = "powerline"
powerline_symbol = ""
foreground = "#000000"
background = "#1976d2"
template = "  {{ .Full }} "
```

## Properties [​](https://ohmyposh.dev/docs/segments/cli/svelte\#properties "Direct link to Properties")

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `home_enabled` | `boolean` | `false` | display the segment in the HOME folder or not |
| `fetch_version` | `boolean` | `true` | fetch the svelte version |
| `cache_duration` | `string` | `none` | the duration for which the version will be cached. The duration is a string in the format `1h2m3s` and is parsed using the [time.ParseDuration](https://golang.org/pkg/time/#ParseDuration) function from the Go standard library. To disable the cache, use `none` |
| `missing_command_text` | `string` |  | text to display when the command is missing |
| `display_mode` | `string` | `files` | - `always`: the segment is always displayed<br>- `files`: the segment is only displayed when file `extensions` listed are present<br>- `context`: displays the segment when the environment or files is active |
| `version_url_template` | `string` |  | a go [text/template](https://golang.org/pkg/text/template/) [template](https://ohmyposh.dev/docs/configuration/templates) that creates the URL of the version info / release notes |
| `extensions` | `[]string` | `svelte.config.js` | allows to override the default list of file extensions to validate |
| `folders` | `[]string` |  | allows to override the list of folder names to validate |

## Template ( [info](https://ohmyposh.dev/docs/configuration/templates)) [​](https://ohmyposh.dev/docs/segments/cli/svelte\#template-info "Direct link to template-info")

default template

```template
{{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }}
```

### Properties [​](https://ohmyposh.dev/docs/segments/cli/svelte\#properties-1 "Direct link to Properties")

| Name | Type | Description |
| --- | --- | --- |
| `.Full` | `string` | the full version |
| `.Major` | `string` | major number |
| `.Minor` | `string` | minor number |
| `.Patch` | `string` | patch number |
| `.URL` | `string` | URL of the version info / release notes |
| `.Error` | `string` | error encountered when fetching the version string |

- [What](https://ohmyposh.dev/docs/segments/cli/svelte#what)
- [Sample Configuration](https://ohmyposh.dev/docs/segments/cli/svelte#sample-configuration)
- [Properties](https://ohmyposh.dev/docs/segments/cli/svelte#properties)
- [Template (info)](https://ohmyposh.dev/docs/segments/cli/svelte#template-info)
  - [Properties](https://ohmyposh.dev/docs/segments/cli/svelte#properties-1)