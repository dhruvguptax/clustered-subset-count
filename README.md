# Clustered Subset Count

This repository introduces a new combinatorial function called the Clustered Subset Count.

## Definition

The Clustered Subset Count function, denoted as C(n, k; d), counts the number of subsets of a finite integer set where all elements are mutually within a limited distance from each other.

**Formula:**

C(n, k; d) = |{A ⊆ {1, ..., n} : |A| = k, ∀a ∈ A, ∃b ∈ A \ {a}, |a - b| ≤ d}|


Where:

*   n: The size of the integer set {1, 2, ..., n}.
*   k: The size of the subset being considered.
*   d: The clustering distance parameter.

## Example

C(5, 3; 2) = 8

The clustered subsets are: {1,2,3}, {1,2,4}, {1,3,4}, {1,3,5}, {2,3,4}, {2,3,5}, {2,4,5}, {3,4,5}

## Further Information

See the attached paper for more details.


