"""
CS361 - HW2
Problem 1 - Tower of Hanoi
Author: Shrey Poshiya
"""

def hanoi(n, source="A", auxiliary="B", target="C"):
    if n <= 0:
        return

    # move n-1 disk from source to auxiliary (target is now aux)
    hanoi(n - 1, source, target, auxiliary)
    # place the nth disk on the target rod
    print(f"move disk {n} from {source} to {target}")
    # move n-1 disk from auxiliary to target
    hanoi(n - 1, auxiliary, source, target)

def main():
    hanoi(3)

if __name__ == "__main__":
    main()

