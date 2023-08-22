#include<bits/stdc++.h>

using namespace std;

int recSum(int num, int sum){
    if(num == 0)
        return sum;

    sum += num;
    recSum(num-1, sum);

}

int main(){
    int num;
    cout<<"Enter the range: ";
    cin>>num;

    cout<<"\n The sum is: "<<recSum(num, 0);

    return 0;
}