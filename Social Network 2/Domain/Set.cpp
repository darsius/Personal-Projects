#include <cstring>
#include "Set.h"

template<class T>
Set<T>::Set() {
}

template<class T>
void Set<T>::add(T elem) {
    if (!elems.searchElement(elem))
    elems.add(elem);
}

template<class T>
bool Set<T>::search(T elem) {
    return elems.searchElement(elem);
}


template<class T>
void Set<T>::remove(T elem) {
    elems.removeElement(elem);
}

template<class T>
void Set<T>::showAll() {
    elems.showAll();
}

template<class T>
void Set<T>::update(T elem, T newElem) {
    elems.removeElement(elem);
    elems.add(newElem);
}

template<class T>
vector<T> Set<T>::getAll() {
    return this->elems.getAll();
}




