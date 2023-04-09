//
// Created by p_dar on 5/17/2022.
//

#include "ServiceMessage.h"

ServiceMessage::ServiceMessage() {
    
}

ServiceMessage::ServiceMessage(RepositoryMessage<Message> &repository) {
    this->repositoryMessage = repository;
}

void ServiceMessage::addMessage(string name1, string name2, string text) {
    Message m(name1, name2, text);
    this->repositoryMessage.add(m);
}

void ServiceMessage::removeMessage(string name1, string name2, string text) {
    Message m(name1, name2, text);
    this->repositoryMessage.remove(m);
}

Message *ServiceMessage::getAll() {
    return this->repositoryMessage.getAll();
}

ServiceMessage::~ServiceMessage() {

}

int ServiceMessage::getSize() {
    return this->repositoryMessage.size();
}

vector<string> ServiceMessage::showMessagesForAnUser(string name) {
    Message* rez = repositoryMessage.getAll();
    vector<string >lst;
    for (int i = 0; i < repositoryMessage.size(); i++ ){
        if ( rez[i].getName1() == name){
            lst.push_back(rez[i].getName2());
            lst.push_back(rez[i].getText());
        }
        if ( rez[i].getName2() == name){
            lst.push_back(rez[i].getName1());
            lst.push_back(rez[i].getText());
        }
    }
    return lst;
}
