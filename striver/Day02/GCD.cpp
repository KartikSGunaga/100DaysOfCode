#include<bits/stdc++.h>

using namespace std;

int gcd(int, int);

int main(){
    int num1, num2;

    cout<<"enter the two numbers: ";
    cin>>num1>> num2;

    if(num2 < num1){
        int temp = num1;
        num1 = num2;
        num2 = temp;
    }

    cout<<"\n the GCD is: "<<gcd(num1, num2);

    return 0;
}

int gcd(int num1, int num2){
    int result = 1;
    for(int i = 1; i <= num1; i++){
        if(num1 % i == 0 && num2 % i == 0){
            result = i;
        }
    }
    return result;
}