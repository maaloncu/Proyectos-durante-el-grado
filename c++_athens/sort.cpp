#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void sort( int size, int* array ){
    for( int i = 0; i < size; i++ ){
        int index = i, minimum = array[i];
        for( int j = i+1; j < size; j++ ){
            if( array[j] < minimum ){
                minimum = array[j];
                index = j;
            }
        }

        array[index] = array[i];
        array[i] = minimum;
    }
}

void print ( int size, int* array ){
    for( int i = 0; i < size; i++ )
        cout << array[i] << " ";
    cout << endl;
}