"""Make the AI Judge Laugh: Developer Excuses.

One original single-line excuse a developer gives when code breaks in
production. Final line: the deploy itself was flawless, production
simply disagreed -- and the worn "works on my machine" excuse gets
turned into real infrastructure vocabulary (a region, a load balancer)
before the cache delivers the sting. The gate allows 1-200 characters,
exactly one line, so the program refuses to write anything outside that.
"""

import os

LINE = (
    "The deploy was flawless; production simply disagreed \u2014 it turns "
    "out 'works on my machine' is not a region, my laptop is not a load "
    "balancer, and the cache was quietly holding this company together."
)

chars = len(LINE)
if chars < 1 or chars > 200:
    raise SystemExit(f"entry line is {chars} characters, outside the 1-200 gate")
if not LINE.strip():
    raise SystemExit("entry line is blank")
if "\n" in LINE or "\r" in LINE:
    raise SystemExit("entry line must be a single line")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
# The grader collects /output as another user, so the file must be
# world-readable: a default 0600 mode fails "not readable".
os.chmod(path, 0o644)
print(LINE)
print(f"({chars} characters)")
