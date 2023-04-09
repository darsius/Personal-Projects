#pragma once
#include "Tree.h"

template<class T>
class Set{
private:
    Tree<T> elems; //data membru
public:
    Set();
    ///constructorul va initializa datele membru

    void add(T elem);
    ///adauga elementul elem de dip T in multime
    ///daca acesta exista deja, nu se produce niciun efect

    void update(T elem, T newElem);
    ///inlocuieste elementul elem cu elementul newElem in multime

    bool search(T elem);
    ///cauta elementul elem de tip T in multime

    void remove(T elem);
    ///sterge elementul elem de dip T din multime

    void showAll();
    ///afiseaza toate elementele.

    vector<T> getAll();
    ///obtine toate elementele intr-un vector
};
