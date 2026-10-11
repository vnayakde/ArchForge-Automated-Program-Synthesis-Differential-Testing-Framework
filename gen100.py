import os
import sys

def main():
    # Support both in-tree binary and build/ directory binary
    candidates = [
        os.path.join("build", "src", "csmith"),
        os.path.join("src", "csmith"),
        "csmith"
    ]
    binary = None
    for cand in candidates:
        if os.path.exists(cand) or cand == "csmith":
            binary = cand
            break

    count = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    out_dir = "tests"
    os.makedirs(out_dir, exist_ok=True)

    print(f"Generating {count} random C test cases into ./{out_dir}/...")
    for seed in range(count):
        out_file = os.path.join(out_dir, f"test_{seed}.c")
        cmd = f"{binary} -s {seed} -o {out_file}"
        ret = os.system(cmd)
        if ret != 0:
            print(f"Failed to generate seed {seed}. Ensure generator binary is built.")
            break
        print(f"[{seed + 1}/{count}] Generated {out_file}")

if __name__ == "__main__":
    main()
