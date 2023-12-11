
#include<iostream>
using namespace std;
int main() {
  int n;
  cin>>n;
  int s=n*(n+1)/2;
  for(int i=0;i<n-1;i++){
      int k;
      cin>>k;
      s-=k;
  }
  cout<<s<<endl;

    return 0;
}