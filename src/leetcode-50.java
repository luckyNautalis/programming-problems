// Problem 50: Pow(x,n)

/**
 * Constraints
 *
 * 1) -100.0 < x < 100.0
 * 2) -2^{31} <= n <= 2^{31}-1
 * 3) n is an integer
 * 4) Either x is not zero or n > 0
 * 5) -10^4 <= xn <= 10^4
 *
 */

class Solution {

    public double myPow(double x, int n) {

        double pow = x;
        if (x == 0) {
           pow = 0;
        }
        else if (x == -1 && (n % 2) != 0) {
           pow = -1;
        }
        else if ((x == -1 && (n % 2) == 0) || (x == 1)) {
            pow = 1;
        }
        else if (n <= -1) {

            pow = 1/pow;
            for (int i = -2; i >= n; i--) {

                pow = pow * 1/x;
                if ((x < 0) && ((pow < -10e-10 && pow > -10e-100) || pow < -10e8)) {
                    break;
                }
                else if (((pow < 10e-10 && pow > 10e-100) || pow > 10e8)) {
                    break;
                }
            }
        }
        else if (n == 0) {
            pow = 1;
        }
        else if (n > 1) {

            for (int i = 2; i <= n; i++) {

                pow = pow * x;
                if ((x < 0) && ((pow < -10e-10 && pow > -10e-100) || pow < -10e8)) {
                    break;
                }
                else if (((pow < 10e-10 && pow > 10e-100) || pow > 10e8)) {
                    break;
                }
            }
        }
        return pow;
    }
}
