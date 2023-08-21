#include<bits/stdc++.h>

using namespace std;

int main(){
    cout<<"Enter the count: ";
    int n, i;

    cin>>n;

    for(i = 0; i < n; i++){
        cout<<"\n";
        for(int j = 0; j <= i; j++){
            cout<<"*";
        }
    }

    return 0;
}