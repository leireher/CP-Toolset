#include "mathlib.hpp"

namespace mathlib {
    /*
    * Fast exponentiation using 2^k-ary algorithm
    * For more details see: https://en.wikipedia.org/wiki/Exponentiation_by_squaring#2k-ary_method
    */
    long long exp_by_squaring(long long base, long long exp, long long modulo) {
        long long t = 1ll;
        while (exp > 0) {
            if (exp % 2 != 0) t = (t * base) % modulo;
            base = (base * base) % modulo;
            exp /= 2;
        }
        return t % modulo;
    }
}
