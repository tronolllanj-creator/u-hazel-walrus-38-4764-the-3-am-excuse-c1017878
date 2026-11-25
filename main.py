import os
import sys

"""
# 3 AM excuse: the wallet refuses to sign; the line is fixed, the program only writes it.
Writes a single creative excuse from a hardware wallet refusing to sign a 3 AM transaction.
The excuse personifies the wallet's seed phrase as observing union office hours.
# Entry validated: output is 1-200 chars, one line, deterministic.
"""

LINE = "I have officially converted myself into a pretentious paperweight for the night because my seed phrase strictly observes union office hours and categorically rejects your 3 AM crypto delusions."

def main() -> None:
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', 'out')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'entry.txt')
    
    content = LINE + '\n'
    
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError('Content validation failed: must be 1-200 chars including newline, not only whitespace')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'{output_path} {len(content)}')

if __name__ == '__main__':
    main()
