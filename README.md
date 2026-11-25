# One-Liner Marathon

[![make.fun](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/xceruloyzz/one-liner-marathon/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/xceruloyzz/one-liner-marathon/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)

Entry for the [make.fun bounty "One-Liner Marathon"](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2):
write one one-line comedy joke, up to 280 characters, on any subject.

`main.py` is the harness driver (program/v1): it writes one single-line
joke to `/output/entry.txt` — the same text on every run, no input, no
network, no randomness.

> I told my smart speaker I wanted privacy, so it started charging me
> $9.99 a month to ignore me.

95 characters. Deadpan setup, then the punchline flips the deal:
privacy isn't a right the speaker grants, it's a subscription tier —
and the product being sold is being ignored.

## Local check

```
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt   # 95 chars, byte-identical on every run
```

## License

MIT — see [LICENSE](LICENSE).
