#include<iostream>

using namespace  std;

void main(){
    //하나가 주소값, 레퍼런스로 입력받는 함수
    int a=0,b=0; 
    cin>>a>>b;
    swap(a,b);

}

void swap(int *a,int &b){
    int temp;
    *a=b;
    temp = *a;
    b = temp;
}

