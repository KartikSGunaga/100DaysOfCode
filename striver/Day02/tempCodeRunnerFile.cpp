using namespace std;

int main(){
    int num, temp, rev = 0;

    cout<<"Enter the number: ";
    cin>>num;

    temp = num;

    while(temp > 0){
        rev = rev*10 + (temp % 10);
        temp /= 10;
    }
    cout<<"the reverse of "<<num<<" is: "<<rev;

    return 0;
}