#include<bits/stdc++.h>

using namespace std;

int main(){
    cout<<"Enter the count: ";
    int n, i;

    cin>>n;

    for(i = n; i >= 0; i--){
        cout<<"\n";
        for(int j = 0; j < i; j++){
            cout<<j + 1;
        }
    }

    return 0;
}