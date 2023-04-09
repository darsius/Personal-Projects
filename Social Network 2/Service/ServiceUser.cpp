//
// Created by p_dar on 4/29/2022.
//

#include "ServiceUser.h"
#include "../Domain/User.h"

ServiceUser::ServiceUser() {
}

ServiceUser::ServiceUser(RepositoryUser<User> &repository) {
    this->repository = repository;
}

void ServiceUser::addUser(int id, string name) {
    User u(id, name);
    this->repository.add(u);
}

void ServiceUser::removeUser(int id, string name) {
    User u(id, name);
    this->repository.remove(u);
}


//bool ServiceUser::searchUser(int id, string name) {
//    User u(id, name);
//    this->repository.search(u);
//}

void ServiceUser::updateUser(int id, string name, int newId, string newName) {
    User u1(id, name);
    User u2(newId, newName);
    this->repository.update(u1, u2);
}

ServiceUser::~ServiceUser() {

}

void ServiceUser::showAll() {
    this->repository.showAll();
}

vector<User>ServiceUser::getAll() {
    return this->repository.getAll();
}
