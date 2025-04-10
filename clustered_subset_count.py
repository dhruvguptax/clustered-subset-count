import itertools

def is_clustered(subset, d):
    """
    Check if a given subset is clustered with distance d.
    A subset is clustered if every element has at least
    one other element within distance <= d.
    """
    for i in range(len(subset)):
        has_neighbor = any(
            i != j and abs(subset[i] - subset[j]) <= d
            for j in range(len(subset))
        )
        if not has_neighbor:
            return False
    return True

def clustered_subset_count(n, k, d):
    """
    Computes C(n, k; d) = number of size-k clustered subsets of {1..n}
    """
    base_set = list(range(1, n + 1))
    all_subsets = itertools.combinations(base_set, k)
    count = 0

    for subset in all_subsets:
        if is_clustered(subset, d):
            count += 1

    return count

if __name__ == "__main__":
    print("Clustered Subset Count Calculator")
    n = int(input("Enter n (size of full set): "))
    k = int(input("Enter k (size of subsets): "))
    d = int(input("Enter d (clustering distance): "))

    result = clustered_subset_count(n, k, d)
    print(f"C({n}, {k}; {d}) = {result}")
