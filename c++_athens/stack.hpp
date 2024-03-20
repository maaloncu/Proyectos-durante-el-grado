#ifndef STACK_H_
#define STACK_H_

struct mystack {
    int top;
    int* array;
    int size;
    mystack();
    mystack( int size );
    mystack(const mystack& s);
    ~mystack();
    int pop();
    void push(int element);
    bool empty();
    bool full();
    void print();
    void operator+=(int element);
    void operator--();
};


#endif