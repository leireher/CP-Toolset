//Complexity: O(log b)
//Returns (a^b)%c
int modular_pow(int a, int b, int c) {
    int result = 1;
    while (b > 0) {
        if (b % 2 == 1)
            result = (result * a) % c;
        b = b >> 1;
        a = (a * a) % c;
    }
    return result;
}
