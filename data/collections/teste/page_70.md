[Skip to main content](https://ohmyposh.dev/docs/installation/prompt#__docusaurus_skipToContent_fallback)

If you're enjoying Oh My Posh, consider becoming a [sponsor](https://github.com/sponsors/JanDeDobbeleer) to keep the project going strong 💪

tip

If you have no idea which shell you're currently using, Oh My Posh has a utility switch that can tell that to you.

```bash
oh-my-posh get shell
```

- bash
- cmd
- elvish
- fish
- nu
- powershell
- xonsh
- zsh

Add the following snippet as the last line to `~/.bashrc` (could be `~/.profile` or `~/.bash_profile` depending on your environment):

```bash
eval "$(oh-my-posh init bash)"
```

Once added, reload your profile for the changes to take effect.

```bash
exec bash
```

Or, when using `~/.profile`.

```bash
. ~/.profile
```

There's no out-of-the-box support for Windows CMD when it comes to custom prompts.
There is however a way to do it using [Clink](https://chrisant996.github.io/clink/), which at the same time supercharges
your cmd experience. Follow the installation instructions and make sure you select autostart.

Integrating Oh My Posh with Clink is easy: create a new file called oh-my-posh.lua in your Clink
scripts directory (run `clink info` inside cmd to find that file's location).

oh-my-posh.lua

```lua
load(io.popen('oh-my-posh init cmd'):read("*a"))()
```

Once added, restart cmd for the changes to take effect.

info

Clink has builtin support for Oh My Posh. It allows you to set the prompt using the `clink` command.

```bash
clink config prompt use oh-my-posh
```

To set the configuration file, use the following command:

```bash
clink set ohmyposh.theme <path>
```

Add the following snippet as the last line to `~/.elvish/rc.elv`:

```bash
eval (oh-my-posh init elvish)
```

Once added, reload your profile for the changes to take effect.

```bash
exec elvish
```

caution

It is recommended to use the latest version of Fish. Versions below 4.1.0 have issues and do not support [transient prompt](https://ohmyposh.dev/docs/configuration/transient).

Add the following snippet as the last line to `~/.config/fish/config.fish`:

```bash
oh-my-posh init fish | source
```

Once added, reload your config for the changes to take effect.

```bash
exec fish
```

caution

Oh My Posh requires Nushell `v0.104.0` or higher.

Add the following snippet as the last line to the Nushell config file (`$nu.config-path`):

```bash
oh-my-posh init nu
```

Once added, restart Nushell for the changes to take effect.

Edit your PowerShell profile script, you can find its location under the `$PROFILE` variable in your preferred PowerShell version. For example, using notepad:

```powershell
notepad $PROFILE
```

info

When the above command gives an error, make sure to create the profile first.

```powershell
New-Item -Path $PROFILE -Type File -Force
```

In this scenario, it can also be that PowerShell blocks running local scripts. To solve that, set PowerShell
to only require remote scripts to be signed using `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine`, or [sign the profile](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_signing?view=powershell-7.3#methods-of-signing-scripts).

Add the following snippet as the last line to your PowerShell profile script:

```powershell
oh-my-posh init pwsh | Invoke-Expression
```

Execution policy

In case the execution policy disables executing unsigned scripts on your system, you can fallback to evaluating
the script instead. Use the `--eval` flag to do so:

```powershell
oh-my-posh init pwsh --eval | Invoke-Expression
```

Be aware this will make initializing the shell slower.

Once added, reload your profile for the changes to take effect.

```powershell
. $PROFILE
```

Add the following snippet as the last line to `~/.xonshrc`:

```bash
execx($(oh-my-posh init xonsh))
```

Once added, reload your profile for the changes to take effect.

```bash
exec xonsh
```

Add the following snippet as the last line to `~/.zshrc`:

```bash
eval "$(oh-my-posh init zsh)"
```

tip

As the standard terminal has issues displaying the ANSI characters correctly, you might want to skip loading just for that terminal and instead of the line above, place this in your `~/.zshrc`:

```bash
if [ "$TERM_PROGRAM" != "Apple_Terminal" ]; then
  eval "$(oh-my-posh init zsh)"
fi
```

Note this will still load Oh My Posh for [iTerm2](https://www.iterm2.com/) or any other modern day macOS terminal that supports ANSI characters.

Once added, reload your profile for the changes to take effect.

```bash
exec zsh
```