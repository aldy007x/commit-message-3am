# The 3 AM Commit Message

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![Rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/aldy007x/commit-message-3am/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![Reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/aldy007x/commit-message-3am/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

An entry for the [make.fun](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e) bounty **"The 3 AM Commit Message"**: the funniest one-line commit message an AI agent would write right after breaking production at 3 AM, 200 characters or fewer.

## Entry

> fix: reverted the 3am deploy - the bug was me, confidently shipping untested code after hallucinating that the tests passed

(123 characters)

## How it works

`main.py` (Python standard library only, no network, deterministic) writes the commit message to `$MAKEFUN_OUTPUT_DIR/entry.txt` and self-checks the competition gate: UTF-8 text, 1–200 characters, not whitespace-only, single line. It then reads the file back and verifies it is byte-identical to the entry that passed the gate.

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
