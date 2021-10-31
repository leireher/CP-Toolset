#include "stringlib.hpp"

namespace stringlib {
    void count_sort(std::vector<int> &p, std::vector<int> &c) {
        int n = p.size();
        std::vector<int> count(n);
        for (auto x : c) count[x]++;

        std::vector<int> pos(n);
        pos[0] = 0;
        for (int i = 1; i < n; i++) pos[i] = pos[i - 1] + count[i - 1];

        std::vector<int> new_p(n);
        for (auto x: p) {
            new_p[pos[c[x]]] = x;
            pos[c[x]]++;
        }
        p = new_p;
    }

    std::vector<int> build_suffix_array(std::string &s) {
        s += "$";

        int n  = s.size();
        std::vector<int> p(n), c(n);

        std::vector<std::pair<char, int>> a(n);
        for (int i = 0; i < n; i++) {
            a[i] = {s[i], i};
        }
        std::sort(a.begin(), a.end());

        for (int i = 0; i < n; i++) p[i] = a[i].second;
        c[p[0]] = 0;
        for (int i = 1; i < n; i++) {
            c[p[i]] = (a[i].first == a[i - 1].first) ? c[p[i - 1]] : c[p[i - 1]] + 1;
        }

        int k = 0;
        while ((1 << k) < n) {
            for (int i = 0; i < n; i++) p[i] = (p[i] - (1 << k) + n) % n;

            stringlib::count_sort(p, c);

            std::vector<int> c_new(n);
            c_new[p[0]] = 0;

            for (int i = 1; i < n; i++) {
                std::pair<int, int> current = {c[p[i]], c[(p[i] + (1 << k)) % n]};
                std::pair<int, int> prev = {c[p[i - 1]], c[(p[i - 1] + (1 << k)) % n]};
                c_new[p[i]] = (current == prev) ? c_new[p[i - 1]] : c_new[p[i - 1]] + 1;
            }
            c = c_new;
            k++;
        }
        s.pop_back();

        return p;
    }
}
