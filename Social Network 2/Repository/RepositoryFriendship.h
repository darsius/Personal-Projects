
#pragma once

#include "../Domain/List.h"
#include "RepositoryUser.h"
#include "../Domain/Friendship.h"


template <class T>
class RepositoryFriendship {
private:
    List<T> listFriendship;
    RepositoryUser<User> r;
public:
    RepositoryFriendship() {
    }
    ///constructorul va initializa datele membru


    void add(const T& elem) {
        listFriendship.add(elem);
    }
    ///adauga elementul elem de dip T in repository-ul prietenie


    void remove(const T& elem) {
        listFriendship.remove(elem);
    }
    ///sterge elementul elem de dip T din repository-ul prietenie


    T* getAll() {
        return this->listFriendship.getAll();
    }
    ///returneaza adresa eleementelor de tip T

    int size() {
        return this->listFriendship.length();
    }
    ///returneaza cate elemente de tip T sunt in repository-ul prietenie

    void update(const T& elem, const T& elemNou) {
        this->lista.updateUser(elem, elemNou);
    }
    ///inlocuieste elementul elem cu elementul newElem in repository-ul prietenie


//    bool isFull() {
//        return this->length == l;
//    }

    ~RepositoryFriendship(){};
    ///destructorul
};