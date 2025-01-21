// main.cc
#include <algorithm>
#include <vector>
#include <iostream>

void mysort(std::vector<int>& data) {
    std::sort(data.begin(), data.end());
}

int main() {
    std::vector<int> data = {5, 3, 8, 1};
    mysort(data);
    for (int num : data) {
        std::cout << num << " ";
    }
    return 0;
}
