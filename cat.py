'''
This program prints stdin to the screen.
'''
import sys
import shutil

def cat(file):
    # Copy in fixed-size chunks so memory stays O(1) for any input size.
    shutil.copyfileobj(file, sys.stdout.buffer, length=64 * 1024)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
