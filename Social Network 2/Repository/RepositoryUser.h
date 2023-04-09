
#pragma once

#include "../Domain/Set.cpp"
#include "../Domain/User.h"
#include <vector>

template <class T>
class RepositoryUser {
private:
    Set <T> list;
public:
    RepositoryUser() {
    }
    ///constructorul va initializa datele membru

    bool search(const T& elem){
        return list.search(elem);
    }
    ///cauta elementul elem de tip T in repository-ul utilizator


    void add(const T& elem) {
        if (!list.search(elem))
            list.add(elem);
    }
    ///adauga elementul elem de dip T in repository-ul utilizator

    void remove(const T& elem) {
        list.remove(elem);
    }
    ///sterge elementul elem de dip T din repository-ul utilizator

    void showAll() {
        list.showAll();
    }
    ///afiseaaza toti utilizatorii

    vector<T> getAll(){
        return this->list.getAll();
    }
    ///memoreaza intr-un vector toate elementele de tip T.

    void update(const T& elem, const T& elemNou) {
        if (!list.search(elemNou))
            list.update(elem, elemNou);
    }
    ///inlocuieste elementul elem cu elementul newElem in repository-ul prietenie


    ~RepositoryUser(){};
    ///destructorul

};
