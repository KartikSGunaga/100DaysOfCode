#include<bits/stdc++.h>

using namespace std;

int main(){
    int num, i;

    cout<<"Enter the number: ";
    cin>>num;

    for(i = 2; i < num; i++){
        if(num % i == 0){
            cout<<"It is not prime number.";
            return 0;
        }
    }
    cout<<"It is a prime number.";
    return 0;
}