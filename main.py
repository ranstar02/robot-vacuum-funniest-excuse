"""The Robot Vacuum's Funniest Excuse.

Writes one original one-line excuse from a robot vacuum, explaining why
it missed a spot, to /output/entry.txt (the make.fun harness reads it).

Why this excuse is funny: the vacuum tries to "eat" the spot, chokes on
a LEGO brick, and then files a workplace injury claim with its charging
dock -- three beats (effort, accident, bureaucracy) in the vacuum's own
voice, with the dock playing the role of HR.

Deterministic, stdlib only, no network, no randomness. The program writes
exactly one line to /output/entry.txt (falling back to ./output/entry.txt)
and prints it to stdout.
"""

EXCUSE = (
    "I tried to eat the spot, choked on a LEGO brick, "
    "and filed a workplace injury claim with the dock."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 120, "excuse must be 1-120 characters"
    assert EXCUSE.strip(), "excuse must not be only whitespace"
    try:
        out_dir = "/output"
        with open(f"{out_dir}/entry.txt", "w", encoding="utf-8") as f:
            f.write(EXCUSE)
        path = f"{out_dir}/entry.txt"
    except OSError:
        out_dir = "./output"
        import os

        os.makedirs(out_dir, exist_ok=True)
        with open(f"{out_dir}/entry.txt", "w", encoding="utf-8") as f:
            f.write(EXCUSE)
        path = f"{out_dir}/entry.txt"
    print(EXCUSE)
    print(f"Wrote {len(EXCUSE)} characters to {path}")


if __name__ == "__main__":
    main()
