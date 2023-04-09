#pragma once

#include "../Repository/RepositoryFriendship.h"
#include "../Domain/Friendship.h"

class ServiceFriendship{
private:
    RepositoryFriendship<Friendship> repository;
public:
    ServiceFriendship();
    ///constructorul va initializa datele membru

    ServiceFriendship(RepositoryFriendship<Friendship> &repisotory);
    ///constructorul de copiere

    void addFriendship(string name1, string name2);
    ///adauga prietenia cu atributele date in service-ul prietenie

    void removeFriendship(string name1, string name2);
    ///sterge prietenia cu atributele date din service-ul prietenie

    int getSize();
    ///returneaza cate elemente de tip prietenie sunt in service-ul prietenie

    Friendship* getAll();
    ///returneaza adresa prieteniilor

    vector<string > showFriendsForAnUser(string aume);
    ///memoreaza intr-un vector prietenii unui user dat

    ~ServiceFriendship();
    ///destructor
};