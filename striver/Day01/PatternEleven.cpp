#include<bits/stdc++.h>

using namespace std;

int main(){
    int n, i, j, k;

     cout<<"Enter the count: ";
     cin>>n;

     for(i = 0; i < n; i++){
        cout<<"\n";
        for(j = 0; j <= i; j++){
            cout<<j+1;
        }
        for(k = i*2 + 1; k <= n + 1; k++){
            cout<<" ";
        }
        for(j = j; j > 0; j--){
            cout<<j;
        }
     }
}