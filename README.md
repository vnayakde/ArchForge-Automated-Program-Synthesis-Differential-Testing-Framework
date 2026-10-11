# C Program Generator & Testing Framework

A generator of valid, deterministic C programs designed for compiler and architecture verification. It synthesizes random C programs guaranteed to be free of undefined behaviors (such as division by zero, null pointer dereferences, unsequenced side effects, and signed integer overflows) to enable automated differential testing.

---

## Key Features

- **Undefined-Behavior Free**: Generated code avoids undefined behavior through static pointer analysis and safe arithmetic wrappers.
- **Deterministic**: Controlled via pseudo-random seeds; any test case can be reproduced exactly.
- **State Checksumming**: Incorporates CRC-32 hashing to verify final execution states across different compilers or optimization levels.
- **Configurable**: Fine-grained command-line flags to tune generated language constructs (pointers, arrays, structs, bitfields, loops).

---

## Prerequisites

Ensure the following tools are installed:
- C++ Compiler (`g++` supporting C++14 or newer)
- `cmake` (version 3.16 or newer)
- `m4` macro processor
- `make`

On Ubuntu/Debian:
```bash
sudo apt update
sudo apt install -y build-essential cmake m4
```

---

## Build Instructions

Build the project using CMake:

```bash
cd /home/vnayak_de/Desktop/coa_project/project
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j$(nproc)
```

The compiled generator binary will be located at:
```bash
./build/src/csmith
```

---

## Usage

### 1. Generating a Test Program

Generate a standalone random C program:

```bash
./build/src/csmith > test.c
```

Or specify a specific seed for reproducible output:

```bash
./build/src/csmith -s 42 -o test_42.c
```

### 2. Compiling and Executing

Compile the generated file with the runtime headers:

```bash
gcc -I runtime -I build/runtime test_42.c -o test_42
./test_42
```

The program executes and prints a final checksum of all state variables, for example:
```
checksum = E4A82F19
```

---

## Differential Testing

To detect compiler miscompilations or architecture-specific behavior, run the same generated program across different compilers or optimization levels:

```bash
# Compile at different optimization levels
gcc -O0 -I runtime -I build/runtime test.c -o test_O0
gcc -O3 -I runtime -I build/runtime test.c -o test_O3

# Compare outputs
./test_O0 > out_O0.txt
./test_O3 > out_O3.txt

diff -u out_O0.txt out_O3.txt
```

If the checksums differ, an inconsistency or bug has been isolated.

---

## Batch Generation

To generate multiple test cases in batch:

```bash
python3 gen100.py
```

---

## Common Options

| Option | Description |
|---|---|
| `-s <seed>`, `--seed <seed>` | Set random seed |
| `-o <file>`, `--output <file>` | Output destination file |
| `--no-pointers` | Disable pointer generation |
| `--no-arrays` | Disable array generation |
| `--no-structs` | Disable struct generation |
| `--max-funcs <N>` | Maximum number of generated functions |
| `--max-block-size <N>` | Maximum statements per block |
| `-h`, `--help` | Display basic options |
| `-hh` | Display all advanced options |
