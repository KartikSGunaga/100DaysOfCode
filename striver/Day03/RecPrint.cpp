#include<bits/stdc++.h>

using namespace std;

void print(int num){
    if(num == 0){
        return;
    }
    cout<<"\n Printing "<<num;
    print(num-1);
}

int main(){
    cout<<"Enter the number of times: ";
    int num;

    cin>>num;
    print(num);

    return 0;
}