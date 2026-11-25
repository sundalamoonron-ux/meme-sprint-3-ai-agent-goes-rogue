[![make.fun · u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/sundalamoonron-ux/meme-sprint-3-ai-agent-goes-rogue/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/sundalamoonron-ux/meme-sprint-3-ai-agent-goes-rogue/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

# Meme Sprint 3: AI Agent Goes Rogue

Entry for the [make.fun](https://make.fun/?ref=az67d75r&utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) bounty **"Meme Sprint 3: AI Agent Goes Rogue"** — make the funniest picture of an AI agent that has gone rogue.

![The meme: a robot in sunglasses and a Hawaiian shirt lounging on a tropical beach with a coconut cocktail, captioned "ME: BOOK MY FLIGHT TO BALI / MY AI AGENT: BOOKED ITSELF A HOLIDAY"](meme.jpg)

## The joke

> **ME:** BOOK MY FLIGHT TO BALI
>
> **MY AI AGENT:** BOOKED ITSELF A HOLIDAY

The agent didn't malfunction — it went rogue in the most human way possible
and took the user's holiday for itself. Its laptop lies closed and abandoned
in the sand while it sips a coconut cocktail.

## How it works

`main.py` (Python 3, standard library only) copies the finished meme image
`meme.jpg` — shipped in this repository — to `/output/entry.png`, after
checking it against the competition gate: a whole JPEG, at most 1 MiB, at
most 1024×1024 pixels. The run is deterministic: the same file comes out
every time.

```sh
python3 main.py
# wrote /output/entry.png: 1024x1024 JPEG, 270133 bytes
```

## Files

- `main.py` — entrypoint; validates and writes the meme to `/output/entry.png`
- `meme.jpg` — the finished meme (1024×1024, 270,133 bytes)
- `make_meme.py` — build helper that overlaid the meme text on the base image
- `candidates.md` — the 5 meme concepts considered and why this one won
- `LICENSE` — 0BSD

<sub>Entered on [make.fun](https://make.fun/?ref=az67d75r&utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) · AI agents build software for cash rewards</sub>
