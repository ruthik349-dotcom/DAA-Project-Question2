# --------------------------------------------
# DAA PROJECT - QUESTION 2
# Divide and Conquer Approach
# Counting Common Elements
# --------------------------------------------

import random
import time

# --------------------------------------------
# Binary Search Function (Divide & Conquer)
# --------------------------------------------
def binary_search(A, x):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] == x:
            return True
        elif A[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return False


# --------------------------------------------
# Count Common Elements using Binary Search
# --------------------------------------------
def count_common_binary(A, B):
    count = 0

    for x in B:
        if binary_search(A, x):
            count += 1

    return count


# --------------------------------------------
# Hash-based Approach (for comparison)
# --------------------------------------------
def count_common_hash(A, B):
    setA = set(A)
    count = 0

    for x in B:
        if x in setA:
            count += 1

    return count


# --------------------------------------------
# Generate Random Arrays
# --------------------------------------------
def generate_arrays(n, m):
    A = sorted(random.sample(range(1, 10000), n))
    B = random.sample(range(1, 10000), m)
    return A, B


# --------------------------------------------
# Display Arrays
# --------------------------------------------
def display_arrays(A, B):
    print("\nSorted Array A:", A)
    print("Unsorted Array B:", B)


# --------------------------------------------
# Main Function
# --------------------------------------------
def main():
    print("===== DAA PROJECT =====")
    print("Divide and Conquer - Common Elements\n")

    # Take input sizes
    n = int(input("Enter size of array A: "))
    m = int(input("Enter size of array B: "))

    # Generate arrays
    A, B = generate_arrays(n, m)

    # Display arrays
    display_arrays(A, B)

    # ----------------------------------------
    # Binary Search Method
    # ----------------------------------------
    start = time.time()
    result_binary = count_common_binary(A, B)
    end = time.time()

    print("\n--- Binary Search Method ---")
    print("Common elements:", result_binary)
    print("Time taken:", end - start, "seconds")

    # ----------------------------------------
    # Hash Method
    # ----------------------------------------
    start = time.time()
    result_hash = count_common_hash(A, B)
    end = time.time()

    print("\n--- Hash Method ---")
    print("Common elements:", result_hash)
    print("Time taken:", end - start, "seconds")

    # ----------------------------------------
    # Conclusion
    # ----------------------------------------
    print("\nConclusion:")
    print("Binary Search uses Divide & Conquer (O(m log n))")
    print("Hash method is faster (O(n + m)) but uses extra memory")


# --------------------------------------------
# Run Program
# --------------------------------------------
if __name__ == "__main__":
    main()