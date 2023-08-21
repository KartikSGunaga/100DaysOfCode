#include<bits/stdc++.h>

using namespace std;

int main(){
    cout<<"Enter the count: ";
    int n, j, i;

    cin>>n;

    for(i = 0; i < n; i++){
        cout<<"\n";
        for(int j = n - i - 1; j >= 0; j--){
            cout<<" ";
        }
        for(j = 1; j <= 2 * i + 1; j++){
            cout<<"*";
        }
        for(int j = n - i - 1; j >= 0; j--){
            cout<<" ";
        }
    }

    return 0;
}