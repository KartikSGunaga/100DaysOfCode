#include<bits/stdc++.h>

using namespace std;

int main(){
    int num, i;

    cout<<"Enter the number: ";
    cin>>num;

    for(i = 1; i <= num; i++){
        if(num % i == 0)
            cout<<i<<", ";
    }

    return 0;
}