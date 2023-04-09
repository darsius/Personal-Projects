
#pragma once

#include "../Domain/List.h"

const int l = 100;

template <class T>
class RepositoryMessage {
private:
    List<T> listMessage;
public:
    RepositoryMessage() {
    }
    ///constructorul va initializa datele membru


    void add(const T& elem) {
        listMessage.add(elem);
    }
    ///adauga elementul elem de dip T in repository-ul mesaje

    void remove(const T& elem) {
        listMessage.remove(elem);
    }
    ///sterge elementul elem de dip T din repository-ul mesaje


    T* getAll() {
        return this->listMessage.getAll();
    }
    ///returneaza adresa eleementelor de tip T


    int size() {
        return this->listMessage.length();
    }
    ///returneaza cate elemente de tip T sunt in repository-ul mesaje


    void update(const T& elem, const T& elemNou) {
        this->lista.updateUser(elem, elemNou);
    }
    ///inlocuieste elementul elem cu elementul newElem in repository-ul prietenie


    bool isFull() {
        return this->length == l;
    }

    ~RepositoryMessage(){};
    ///destructorul

};