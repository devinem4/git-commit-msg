# git-commit-msg
simple commit message checker to ensure `:emoji:`s are valid

## project installation
Copy `commit-msg` and `emoji-checker.py` to `.git/hooks`


## global installation
1. enable git templates
```
$ git config --global init.templateDir ~/.git-templates
```

2. make the `~/.git-templates/hooks` dir
```
$ mkdir -p ~/.git-templates/hooks
```

3. copy `commit-msg` and `emoji-checker.py` to `~/.git-templates/hooks`

4. `git init` in any project dir

5. profit
