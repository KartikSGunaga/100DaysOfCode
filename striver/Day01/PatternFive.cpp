#include<bits/stdc++.h>

using namespace std;

int main(){
    cout<<"Enter the count: ";
    int n, i;

    cin>>n;

    for(i = 0; i < n; i++){
        cout<<"\n";
        for(int j = n - i ; j >= 1; j--){
            cout<<"*";
        }
    }

    return 0;
}