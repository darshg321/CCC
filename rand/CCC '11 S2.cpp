#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<char> studentans(n);
    vector<char> ans(n);

    int right = 0;

    for (int i = 0; i < n; i++) {
        char choice;
        cin >> choice;
        studentans[i] = choice;
    }
    for (int i = 0; i < n; i++) {
        char choice;
        cin >> choice;
        ans[i] = choice;
    }

    for (int i = 0; i < n; i++) {
        if (studentans[i] == ans[i]) {
            right++;
        }
        
    }
    
    cout << right;
    return 0;
}