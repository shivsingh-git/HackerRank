#include <iostream>
#include <string>
using namespace std;

int main() {
    string s1,s2;
	cin>>s1>>s2;
    int len1=s1.size();
    int len2=s2.size();
    cout<<len1<<" "<<len2<<endl;
    string s=s1+s2;
    cout<<s<<endl;
    char c1=s1[0];
    char c2=s2[0];
    s1[0]=c2;
    s2[0]=c1;
    cout<<s1<<" "<<s2;
  
    return 0;
}
