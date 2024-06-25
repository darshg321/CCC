#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string ana1;
    string ana2;

    getline(cin, ana1);
    getline(cin, ana2);

    for (char c : ana1) {
        if (c == ' ') {
            continue;
        }
        
        if (std::count(ana1.begin(), ana1.end(), c) == std::count(ana2.begin(), ana2.end(), c)) {
            continue;
        }
        cout << "Is not an anagram." << endl;
        return 0;
    }

    cout << "Is an anagram." << endl;
    return 0;
}