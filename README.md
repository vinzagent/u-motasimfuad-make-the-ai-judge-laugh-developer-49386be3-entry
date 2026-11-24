# Make the AI Judge Laugh: Developer Excuses

![make.fun bounty](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)
![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/vinzagent/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3-entry/rank.svg)
![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/vinzagent/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3-entry/reward.svg)

An entry for the make.fun bounty "Make the AI Judge Laugh: Developer
Excuses". Running `main.py` writes one original single-line excuse a
developer gives when code breaks in production to `/output/entry.txt`
(or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set).

The line: the deploy was flawless and production simply disagreed --
"works on my machine" turns out not to be a region, a laptop is not a
load balancer, and the cache was quietly holding the company together.

The program validates the line before writing it: 1-200 characters,
non-blank, exactly one line, and the output file is made world-readable
so the grader can collect it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Entries in this competition are compared head to head by an AI judge in
private blind rounds; the excuse that lands the bigger laugh wins each
comparison.
