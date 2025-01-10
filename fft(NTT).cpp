#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdint>

using namespace std;
constexpr int64_t p = 998244353;  // const 지정 안하면 많이 오래걸림

int64_t mod_pow(int64_t base, int64_t exp, int64_t mod) {
    int64_t result = 1;
  
    while (exp > 0) {
        if (exp % 2 == 1)
            result = result * base % mod;
        base = base * base % mod;
        exp /= 2;
    }
  
    return result;
}

void fft(vector<int64_t>& a, bool inv) {
    int64_t n = a.size();
    int64_t j = 0;

    for (int64_t i = 1; i < n; i++) {
        int64_t rev = n / 2;
      
        while (j >= rev) {
            j -= rev;
            rev /= 2;
        }
        j += rev;

        if (i < j)
            swap(a[i], a[j]);
    }

    int64_t step = 2;
    while (step <= n) {
        int64_t half = step / 2;
        int64_t u = mod_pow(3, (p - 1) / step, p);

        if (inv) {
            u = mod_pow(u, p - 2, p);
        }

        for (int64_t i = 0; i < n; i += step) {
            int64_t w = 1;
            for (int64_t j = i; j < i + half; j++) {
                int64_t v = a[j + half] * w % p;
                a[j + half] = (a[j] - v + p) % p;
                a[j] = (a[j] + v) % p;
                w = w * u % p;
            }
        }
        step *= 2;
    }

    if (inv) {
        int64_t num = mod_pow(n, p - 2, p);
        for (int64_t i = 0; i < n; i++) {
            a[i] = a[i] * num % p;
        }
    }
}

string multiply(const string& A, const string& B) {  // multiply numbers
    size_t n = 1;
    while (n < A.size() + B.size() - 1)
        n *= 2;

    vector<int64_t> a(n, 0), b(n, 0);

    for (size_t i = 0; i < A.size(); i++) {
        a[i] = A[A.size() - 1 - i] - '0';
    }
    for (size_t i = 0; i < B.size(); i++) {
        b[i] = B[B.size() - 1 - i] - '0';
    }

    fft(a, false);
    fft(b, false);

    vector<int64_t> c(n);
    for (int64_t i = 0; i < n; i++) {
        c[i] = a[i] * b[i] % p;
    }

    fft(c, true);

    string res;
    int64_t carry = 0;

    for (size_t i = 0; i < c.size(); i++) {
        carry += c[i];
        res += (carry % 10) + '0';
        carry /= 10;
    }

    while (carry) {
        res += (carry % 10) + '0';
        carry /= 10;
    }

    while (res.size() > 1 && res.back() == '0') {
        res.pop_back();
    }
    
    reverse(res.begin(), res.end());
    return res;
}
