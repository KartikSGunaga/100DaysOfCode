#include<bits/stdc++.h>

using namespace std;

int main(){
    int num, i, count = 0;

    cout<<"Enter the number: ";
    cin>>num;
    int temp = num;

    while(temp > 0){
        temp /= 10;
        count++;
    }
    cout<<"\n There are "<<count<<" digits in the number: "<<num;

    return 0;
}