#include<bits/stdc++.h>

using namespace std;

int main(){
    int num, rev = 0;

    cout<<"Enter the number: ";
    cin>>num;

    int temp = num;

    while(temp > 0){
        rev = rev * 10 + temp % 10;
        temp /= 10;
    }
    if(rev == num){
        cout<<"The number "<<num<<" is a palindrome.";
    }
    else{
        cout<<"The number "<<num<<" is not a palindrome.";
    }

    return 0;
}