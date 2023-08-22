#include<bits/stdc++.h>

using namespace std;

void print(int num, int i){
    if(i == num){
        return;
    }
    cout<<"\n Printing "<<++i;
    print(num, i);
}

int main(){
    cout<<"Enter the number of times: ";
    int num, i;

    cin>>num;
    print(num, i = 0);

    return 0;
}