#include <bits/stdc++.h>
#include "stack.hpp"
using namespace std;

mystack::mystack(int size){
    array = new int [size];
    top = 0;
    this->size = size;
}

mystack::mystack(){
    size = 10;
    array = new int [size];
    top = 0;
    this->size = size;
}

mystack::~mystack(){
    cout  << "deleting stack" << endl;
}

mystack::mystack(const mystack& s){
    size = s.size;
    top = s.top;
    array = new int [size];
    for( int i = 0; i < top; i++ ){
        array[i] = s.array[i];
    }
}

int mystack::pop(){
    if( this->empty() ){ cout << "stack is empty" << endl; return 0; }
    return array[--top];
}

void mystack::push(int element){
    if( this->full() ){ cout << "stack is full" << endl; return; }
    array[top++] = element;
}

bool mystack::empty(){
    return top == 0;
}

bool mystack::full(){
    return (top == size);
}

void mystack::print(){
    for( int i = 0; i < top; i++ ){
        cout << array[i] << " ";
    }
    cout << endl;
}

void mystack::operator+=(int element){
    this->push(element);
}

void mystack::operator--(){
    this->pop();
}