# doneberry
![test](https://github.com/yishannn08/robosys2026/actions/workflows/test.yml/badge.svg)

`doneberry` is a command-line bidirectional translator between **Malay** and **Japanese**. It reads text line by line from standard input, detects the source language automatically, and prints the translated result to standard output.

## Purpose & Use Cases

- **Bidirectional Translation**: Converts Malay text into Japanese and Japanese text into Malay without needing any language flags or command-line options.
- **Pipe Support**: Works with standard Unix pipes (|) to translate single lines, multi-line text, or files.
- **Zero External Dependencies**: Implemented using only Python built-in standard libraries (`sys`, `json`, `urllib`), so no `pip install` or virtual environment setup is required.

## Installation

\x60\x60\x60bash
git clone https://github.com/yishannn08/robosys2026.git
cd robosys2026
chmod +x doneberry
\x60\x60\x60

## Usage

Pass input text to `./doneberry` via standard input . Each non-empty line is printed in the format `<original> -> <translated>`.

### 1. Malay to Japanese
```bash
$ echo "anjing" | ./doneberry
anjing -> 犬

### 2. Japanese to Malay

\x60\x60\x60bash
$ echo "ありがとうございます" | ./doneberry
ありがとうございます -> Terima kasih
\x60\x60\x60

## Input Specifications & Error Handling

doneberry checks the input and exits with status 1 when:

- **Empty input** : Prints `No input` and exits with `1`.
- **Non-alphabetic / numeric-only lines** (e.g., `echo "12345" | ./doneberry`): Prints `Invalid input` and exits with `1`.
- **Extra command-line arguments** (e.g., `./doneberry arg1`): Prints `Usage: doneberry < text` and exits with `1`.
- **Network failure**: Prints `Translation error` and exits with `1`.

### Tested Environments
- **OS**: Ubuntu 24.04 
- **Python**: 3.10, 3.11, 3.12, 3.13

## License

- This software package is licensed under the [BSD 3-Clause License](LICENSE).
- © 2026 CHAI YI SHAN

