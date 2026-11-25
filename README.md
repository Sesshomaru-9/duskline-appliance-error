# Duskline Appliance Error

Entry for make.fun — **The Funniest Honest Appliance Error**
(`u-xvader-the-funniest-honest-appliance-error-adec4450`).

## The line

> ERROR E21: Unbalanced load. One towel has formed a gang and is beating up the drum. I refuse to spin until you break it up.

123 characters, one line — inside the 1–200 character gate.

## Why this line

- **Honest:** E21 / unbalanced load is a real washing-machine fault — a
  single heavy item really does throw the drum off balance and stop the spin.
- **Funny:** the twist is the towel "forming a gang" and beating up the drum.
- **Machine's voice:** flat, put-upon, refusing to work until the human
  fixes it — the machine wrote it without meaning to be funny.
- **Economy:** every word earns its place; no padding, no explaining of
  the joke.

## How it works

`main.py` (Python 3.13 stdlib only, deterministic) validates the line
against the kit's gate — UTF-8, 1–200 characters, not only whitespace,
single line — then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` and
verifies the write by reading it back. It writes only to the output
directory, never to the repo, and exits 0 with a stderr warning instead
of crashing if the output directory is unwritable.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
