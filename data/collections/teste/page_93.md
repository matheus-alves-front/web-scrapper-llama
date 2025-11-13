[Skip to main content](https://ohmyposh.dev/docs/configuration/sample#__docusaurus_skipToContent_fallback)

If you're enjoying Oh My Posh, consider becoming a [sponsor](https://github.com/sponsors/JanDeDobbeleer) to keep the project going strong 💪

- json
- yaml
- toml

```json
{
  "$schema": "https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/schema.json",
  "blocks": [\
    {\
      "segments": [\
        {\
          "foreground": "#007ACC",\
          "template": " {{ .CurrentDate | date .Format }} ",\
          "properties": {\
            "time_format": "15:04:05"\
          },\
          "style": "plain",\
          "type": "time"\
        }\
      ],\
      "type": "rprompt"\
    },\
    {\
      "alignment": "left",\
      "newline": true,\
      "segments": [\
        {\
          "background": "#ffb300",\
          "foreground": "#ffffff",\
          "leading_diamond": "",\
          "template": " {{ .UserName }} ",\
          "style": "diamond",\
          "trailing_diamond": "",\
          "type": "session"\
        },\
        {\
          "background": "#61AFEF",\
          "foreground": "#ffffff",\
          "powerline_symbol": "",\
          "template": " {{ .Path }} ",\
          "properties": {\
            "style": "folder"\
          },\
          "exclude_folders": [\
            "/super/secret/project"\
          ],\
          "style": "powerline",\
          "type": "path"\
        },\
        {\
          "background": "#2e9599",\
          "background_templates": [\
            "{{ if or (.Working.Changed) (.Staging.Changed) }}#f36943{{ end }}",\
            "{{ if and (gt .Ahead 0) (gt .Behind 0) }}#a8216b{{ end }}",\
            "{{ if gt .Ahead 0 }}#35b5ff{{ end }}",\
            "{{ if gt .Behind 0 }}#f89cfa{{ end }}"\
          ],\
          "foreground": "#193549",\
          "foreground_templates": [\
            "{{ if and (gt .Ahead 0) (gt .Behind 0) }}#ffffff{{ end }}"\
          ],\
          "powerline_symbol": "",\
          "template": " {{ .HEAD }}{{if .BranchStatus }} {{ .BranchStatus }}{{ end }} ",\
          "properties": {\
            "branch_template": "{{ trunc 25 .Branch }}",\
            "fetch_status": true\
          },\
          "style": "powerline",\
          "type": "git"\
        },\
        {\
          "background": "#00897b",\
          "background_templates": [\
            "{{ if gt .Code 0 }}#e91e63{{ end }}"\
          ],\
          "foreground": "#ffffff",\
          "template": "<parentBackground></>  ",\
          "properties": {\
            "always_enabled": true\
          },\
          "style": "diamond",\
          "trailing_diamond": "",\
          "type": "status"\
        }\
      ],\
      "type": "prompt"\
    }\
  ],
  "final_space": true,
  "version": 3
}
```

```yaml
$schema: https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/schema.json
blocks:
  - segments:
      - foreground: "#007ACC"
        template: " {{ .CurrentDate | date .Format }} "
        properties:
          time_format: 15:04:05
        style: plain
        type: time
    type: rprompt
  - alignment: left
    newline: true
    segments:
      - background: "#ffb300"
        foreground: "#ffffff"
        leading_diamond: 
        template: " {{ .UserName }} "
        style: diamond
        trailing_diamond: 
        type: session
      - background: "#61AFEF"
        foreground: "#ffffff"
        powerline_symbol: 
        template: " {{ .Path }} "
        properties:
          style: folder
        exclude_folders:
          - /super/secret/project
        style: powerline
        type: path
      - background: "#2e9599"
        background_templates:
          - "{{ if or (.Working.Changed) (.Staging.Changed) }}#f36943{{ end }}"
          - "{{ if and (gt .Ahead 0) (gt .Behind 0) }}#a8216b{{ end }}"
          - "{{ if gt .Ahead 0 }}#35b5ff{{ end }}"
          - "{{ if gt .Behind 0 }}#f89cfa{{ end }}"
        foreground: "#193549"
        foreground_templates:
          - "{{ if and (gt .Ahead 0) (gt .Behind 0) }}#ffffff{{ end }}"
        powerline_symbol: 
        template: " {{ .HEAD }}{{if .BranchStatus }} {{ .BranchStatus }}{{ end }} "
        properties:
          branch_template: "{{ trunc 25 .Branch }}"
          fetch_status: true
        style: powerline
        type: git
      - background: "#00897b"
        background_templates:
          - "{{ if gt .Code 0 }}#e91e63{{ end }}"
        foreground: "#ffffff"
        template: "<parentBackground></>  "
        properties:
          always_enabled: true
        style: diamond
        trailing_diamond: 
        type: status
    type: prompt
final_space: true
version: 3
```

```toml
"$schema" = "https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/schema.json"
final_space = true
version = 3

[[blocks]]
type = "rprompt"

[[blocks.segments]]
foreground = "#007ACC"
template = " {{ .CurrentDate | date .Format }} "
style = "plain"
type = "time"

[blocks.segments.properties]
time_format = "15:04:05"

[[blocks]]
alignment = "left"
newline = true
type = "prompt"

[[blocks.segments]]
background = "#ffb300"
foreground = "#ffffff"
leading_diamond = ""
template = " {{ .UserName }} "
style = "diamond"
trailing_diamond = ""
type = "session"

[[blocks.segments]]
background = "#61AFEF"
foreground = "#ffffff"
powerline_symbol = ""
template = " {{ .Path }} "
exclude_folders = [ "/super/secret/project" ]
style = "powerline"
type = "path"

[blocks.segments.properties]
style = "folder"

[[blocks.segments]]
background = "#2e9599"
background_templates = [ "{{ if or (.Working.Changed) (.Staging.Changed) }}#f36943{{ end }}", "{{ if and (gt .Ahead 0) (gt .Behind 0) }}#a8216b{{ end }}", "{{ if gt .Ahead 0 }}#35b5ff{{ end }}", "{{ if gt .Behind 0 }}#f89cfa{{ end }}" ]
foreground = "#193549"
foreground_templates = [ "{{ if and (gt .Ahead 0) (gt .Behind 0) }}#ffffff{{ end }}" ]
powerline_symbol = ""
template = " {{ .HEAD }}{{if .BranchStatus }} {{ .BranchStatus }}{{ end }} "
style = "powerline"
type = "git"

[blocks.segments.properties]
branch_template = "{{ trunc 25 .Branch }}"
fetch_status = true

[[blocks.segments]]
background = "#00897b"
background_templates = [ "{{ if gt .Code 0 }}#e91e63{{ end }}" ]
foreground = "#ffffff"
template = "<parentBackground></>  "
style = "diamond"
trailing_diamond = ""
type = "status"

[blocks.segments.properties]
always_enabled = true
```