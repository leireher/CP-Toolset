#pragma once

#include <vector>
#include <string>
#include <algorithm>

namespace stringlib {
    void count_sort(std::vector<int> &p, std::vector<int> &c);
    std::vector<int> build_suffix_array(std::string &s); 
}
