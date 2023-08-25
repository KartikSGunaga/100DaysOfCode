#include<bits/stdc++.h>

using namespace std;

int main(){
    int n, i, search_ele, arr[100], hash[100], count = 0;

    cout<<"enter the size of the array: ";
    cin>>n;

    for(i = 0; i < n; i++){
        cout<<"\n enter the "<<i+1<<" element: ";
        cin>>arr[i];
    }

    for(int j = 0; j < 100; j++){
        hash[j] == 0;
    }

    for(i = 0; i < n; i++){
        arr[i] = search_ele;
        hash[search_ele]++;
    }

    cout<<"enter the element you want to count: ";
    cin>>search_ele;

    cout<<"\n the element occurs: "<<hash[search_ele]<<" times.";

    return 0;
}