#include "stack.hpp"
#include <iostream>

using namespace std;

int main(){
    mystack s;

    // s.push(10);
    // s.push(10);
    // s.push(10);
    // s.push(10);
    // s.push(10);
    // s.push(50);

    s += 10;
    s += 10;
    s += 10;
    s += 10;
    s += 50;

    s.print();

    if( s.pop() != 50 ){
        cout << "error" << endl;
    }

    --s;

    // while( !s.empty() ) s.pop();
    // while( !s.full() ) s.push(99);

    while (!s.empty() ) --s;
    while (!s.full() ) s += 99;
    

    s.print();

    --s;


    if( s.pop() != 99 )
        cout << "error" << endl;

    cout << "Great succes!" << endl;
    return 0;

    

    
}