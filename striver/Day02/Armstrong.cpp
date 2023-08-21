#include<bits/stdc++.h>

using namespace std;

int main(){
    int num, sum = 0, temp = 0, count = 0, tempnum;

    cout<<"Enter the number: ";
    cin>>num;
    temp = num;

    while(temp> 0){
        count ++;
        temp /= 10;
    }
    temp = num;

    while(temp > 0){
        tempnum = temp % 10;
        sum = sum + pow(tempnum, count);
        temp /= 10;
    }
    if(sum == num){
        cout<<"It is armstrong.";
        return 0;
    }
    cout<<" It is not Armstrong.";
    return 0;
}