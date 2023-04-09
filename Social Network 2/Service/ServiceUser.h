
#pragma once

#include "../Repository/RepositoryUser.h"
#include "../Domain/User.h"

class ServiceUser {
private:
    RepositoryUser <User> repository;
public:
    ServiceUser();
    ///constructorul va initializa datele membru

    ServiceUser(RepositoryUser <User>& repository);
    ///constructorul de copiere


    void addUser(int id, string name);
    ///adauga userul cu atributele date in service-ul user

    void removeUser(int id, string name);
    ///sterge userul cu atributele date din service-ul user

    void updateUser(int id, string name,
                    int newId, string newName);
    ///updateaza userul cu atributele id, name cu userul cu atributele
    ///newId si newName

    void showAll();
    ///afiseaza toti userii

    vector<User> getAll();
    ///memoreaza intr-un vector userii

    ~ServiceUser();
    ///destructor

};
