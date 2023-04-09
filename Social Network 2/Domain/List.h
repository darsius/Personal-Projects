#pragma once
#include "iostream"
using namespace std;


template <class T>
class List{
private:
    T* elems;
    int capacity;
    int noElems;
    void resize();
public:
    List();
    ///constructorul va initializa datele membru

    void add(T elem);
    ///adauga elementul elem de dip T in lista

    void remove(T elem);
    ///sterge elementul elem de dip T din lista

    void update(T elem, T newElem);
    ///inlocuieste elementul elem cu elementul newElem in lista

    int search(T elem);
    ///cauta elementul elem de tip T in lista.

    int length();
    ///returneaza lungimea listei

    T* getAll();
    ///returneaza adresa eleementelor de tip T

    T operator[](int index);
    ///operatorul care coincide cu pozitia elementului in lista

    ~List();
    ///destructorul

};

template<class T>
List<T>::List() {
    capacity = 10;
    noElems = 0;
    this->elems = new T[capacity];
}

template<class T>
void List<T>::add(T elem) {
    if (capacity == noElems)
        resize();
    elems[noElems] = elem;
    noElems ++;
}

template<class T>
void List<T>::resize() {
    T* newElems = new T[capacity * 2];
    for (int i = 0; i < noElems; i++)
        newElems[i] = elems[i];
    capacity = capacity * 2;
    delete[] elems;
    elems = newElems;
}

template<class T>
int List<T>::search(T elem) {
    return 0;
}

template<class T>
int List<T>::length() {
    return noElems;
}

template<class T>
void List<T>::remove(T elem) {
    for (int i = 0; i < noElems; i++)
        if (elems[i] == elem){
            for (int j = i; j < noElems-1; j++)
                elems[j] = elems[j+1];
            noElems --;
        }
}

template<class T>
T* List<T>::getAll() {
    return  this->elems;
}

template<class T>
T List<T>::operator[](int index) {
    return elems[index];
}

template<class T>
List<T>::~List() {
    if (noElems != 0)
        delete [] elems;
    capacity = 10;
    noElems = 0;
}

template<class T>
void List<T>::update(T elem, T newElem) {
    for (int i = 0; i < noElems; i++)
        if (elems[i] == elem)
            elems[i] = newElem;
}

