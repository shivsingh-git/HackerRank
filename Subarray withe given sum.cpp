#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int n,s;
	    cin>>n>>s;
	    int a[n];
	    for(int i=0;i<n;i++)
	    {
	        cin>>a[i];
	    }
	    int sas=0,c=0,flag=0;
        for(int i=0;i<n;i++)
        {
            if(sas+a[i]<=s)
            {
                sas+=a[i];
            }
            else
            {
                sas+=a[i];
                while(sas>s)
                {
                    sas-=a[c];
                    c++;
                }
            }
            if(sas==s)
            {
                cout<<c+1<<" "<<i+1;
                flag=1;
                break;
            }
        }
        if(flag==0)cout<<"-1";
        cout<<endl;
	}
	return 0;
}
