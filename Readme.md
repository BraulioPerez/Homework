# This repository is only for uploading homework

Basically just that

### Exercises
 - Maximum Subarray:
    For this problem i researched for algorithms that allowed me to have a O(n) approach, wich lead me to the kadane's algorithm wich saves a variable called max_sum wich at the beginnin has the smallest value possible, then takes the first numer of the list and starts adding the following numbers of the array, if the sum is bigger than max_sum, max_sum's value changes to it, when it is finished with adding all the numbers to the first, it begins iterating from the second in the list and so on, only updating max_sum if it encounters a bigger value. It's complexity ends up being a higher O(n) value.
    