int main(){
    int arr[100], num, i;

    cout<<"Enter the array length: ";
    cin>>num;

    cout<<"Enter the array elements: ";
    for(i = 0; i < num; i++){
        cin>>arr[i];
    }
    cout<<"\n"<<revArray(arr, num);
}