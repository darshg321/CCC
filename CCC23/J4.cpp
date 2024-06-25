#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    int colnum;
    cin >> colnum;

    vector<int> row1;
    vector<int> row2;
    int tape = 0;

    for (int i = 0; i < colnum; i++) {
        int val;
        cin >> val;
        val == 1 ? tape += 3 : 0;
        row1.push_back(val);
    }
    for (int i = 0; i < colnum; i++) {
        int val;
        cin >> val;
        val == 1 ? tape += 3 : 0;
        row2.push_back(val);
    }

    for (int i = 0; i < colnum-1; i++) {
        if (row1[i] == 1 && row1[i+1] == 1) {
            tape -= 2;
        }
        if (row2[i] == 1 && row2[i+1] == 1) {
            tape -= 2;
        }
    }
    for (int i = 0; i < colnum; i += 2) {
        if (row1[i] == 1 && row2[i] == 1) {
            tape -= 2;
        }   
    }
    
    cout << tape << endl;
    return 0;
}