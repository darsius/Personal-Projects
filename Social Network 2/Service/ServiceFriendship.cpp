

#include "ServiceFriendship.h"
#include <iostream>
using namespace std;

ServiceFriendship::ServiceFriendship() {
}

ServiceFriendship::ServiceFriendship(RepositoryFriendship<Friendship> &repository) {
    this->repository =repository;
}

void ServiceFriendship::addFriendship(string name1, string name2) {
    Friendship f(name1, name2);
    this->repository.add(f);
}

void ServiceFriendship::removeFriendship(string name1, string name2) {
    Friendship f(name1, name2);
    this->repository.remove(f);
}

Friendship* ServiceFriendship::getAll() {
    this->repository.getAll();
}

int ServiceFriendship::getSize() {
    return this->repository.size();
}

vector<string >ServiceFriendship::showFriendsForAnUser(string name) {
    Friendship* rez = repository.getAll();
    vector<string >lst;
    for (int i = 0; i < repository.size(); i++ ){
        if (rez[i].getName1() == name)
            lst.push_back(rez[i].getName2());
        if (rez[i].getName2() == name)
            lst.push_back(rez[i].getName1());
    }
    return lst;
}

ServiceFriendship::~ServiceFriendship() {
}

