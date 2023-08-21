#include<bits/stdc++.h>

using namespace std;

int main(){
    int i, j, n, num = 1;

    cout<<"Enter the count: ";
    cin>>n;

    for(i = 0; i <= n; i++){
        cout<<"\n";
        for(j = 0; j < i; j++){
            cout<<num;
            num ++;
        }
        for(j = n - i -1; j >= 0; j--){
            cout<<" ";
        }
    }
}