#include<bits/stdc++.h>

using namespace std;

int powerof(int power, int base){
    if(power == 0) return 1;

    return(powerof(power - 1, base) * base);
}

int main(){
    int power, base;

    cout<<"Enter the power: ";
    cin>>power;
    cout<<"Enter the base: ";
    cin>>base;

    cout<<"the answer is: "<<powerof(power, base);

    return 0;
}