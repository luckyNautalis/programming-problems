"""1732. Find the Highest Altitude

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude
between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Constraints
-----------
1) n == gain.length
2) 1 <= n <= 100
3) -100 <= gain[i] <= 100
"""


class Solution:

    def largestAltitude(self, gain: List[int]) -> int:
        """
        We can compute the running/net altitudes as we move from one position
        to the next and update the max altitude when necessary. After iteration,
        we then have the highest altitude at some point i.
        """
        max_alt = 0
        alt = 0
        for g in gain:
            alt += g
            max_alt = max(max_alt, alt)
        return max_alt
