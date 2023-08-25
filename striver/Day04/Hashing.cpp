#include<bits/stdc++.h>

using namespace std;

int main(){
    int n, i, search_ele, arr[100], hash[100] = {0}, count;

    cout<<"enter the size of the array: ";
    cin>>n;

    for(i = 0; i < n; i++){
        cout<<"\n enter the "<<i+1<<" element: ";
        cin>>arr[i];
    }

    for(int k = 0; k < n; k++){
        count = arr[k];
        hash[count]++;
    }

    cout<<"enter the element you want to count: ";
    cin>>search_ele;

    cout<<"\n the element occurs: "<<hash[search_ele]<<" times.";

    return 0;
}