#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int kthLargestElement(vector<int>& arr, int k){
    priority_queue<int> pq;
    for(int i = 0; i < arr.size(); i++){
        pq.push(arr[i]);
    }
    int ans;
    while(k){
        ans = pq.top();
        pq.pop();
        k--;
    }

    return ans;
}