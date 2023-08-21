#include <iostream>
 
using namespace std;
 
int main()
{
    int i, j;
    char alpha[100], alphabet;
   
    cout << "Alphabets from (A-Z) are:\n";
   
    // ASCII value of A=65 and Z=90
    for (i = 65; i <= 90; i++) {
        j = 0;
        // Integer i with %c will be converted to character
        // before printing.%c will takes its equivalent
        // character value
        alpha[j] = char(i);
        j++;
    }
    for(j = 0; j < 27; j++){
        cout<<alpha[j];
    }
}