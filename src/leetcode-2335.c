/* 2335. Minimum Amount of Time to Fill Cups

You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.

You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2] denote the number of cold, warm, and hot water cups you need to fill respectively.
Return the minimum number of seconds needed to fill up all the cups.

Constraints
-----------
1) amount.length == 3
2) 0 <= amount[i] <= 100

Example
-------
Input: amount = [1,4,2]
Output: 4
Explanation: One way to fill up the cups is:
Second 1: Fill up a cold cup and a warm cup.
Second 2: Fill up a warm cup and a hot cup.
Second 3: Fill up a warm cup and a hot cup.
Second 4: Fill up a warm cup.
It can be proven that 4 is the minimum number of seconds needed.
*/

int fillCups(int* amount, int amountSize) {
    /*
    Algorithmic Paradigm: Greedy Algorithm
    Programming Paradigm: Imperative
    Complexity:
        - Time: O(1)
        - Space: O(1)
    Explanation: We use a greedy approach by calculating the sum of all cup amounts and the
                 maximum of any single cup amount. The algorithm takes the water sum and divides by 2.
                 The quotient q is how many two cups we can fill at once (+1 second, sec = q).
                 If there is only one cup's worth left to fill, then sec = q + 1. Otherwise,
                 if we could not fill two cups at once or there is more than one cup's worth to
                 fill (after filling duos), we return the max of single cup amounts.
    */
    int max = 0;
    int sum = 0;
    for (int i = 0; i < amountSize; i++) {
        max = amount[i] > max ? amount[i]: max;
        sum += amount[i];
    }
    int sec = sum / 2 + 1;
    return sec > max ? sec : max;
}
