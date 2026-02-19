import subprocess
import sys

RUNS = 5
SCRIPTS = [
    ("1_simple_pg_gymnasium.py", "results_simple_pg.txt"),
    ("reward_to_go.py",          "results_reward_to_go.txt"),
]

for script, output_file in SCRIPTS:
    with open(output_file, "w") as f:
        for run in range(1, RUNS + 1):
            print(f"[{script}] Run {run}/{RUNS}...")
            f.write(f"=== Run {run} ===\n")
            result = subprocess.run(
                [sys.executable, script],
                capture_output=True,
                text=True
            )
            f.write(result.stdout)
            if result.stderr:
                f.write(result.stderr)
            f.write("\n")
    print(f"Results saved to {output_file}\n")
