#pragma once

#include "../Domain/Message.h"
#include "../Repository/RepositoryMessage.h"
#include <vector>

class ServiceMessage{
private:
    RepositoryMessage<Message> repositoryMessage;
public:
    ServiceMessage();
    ///constructorul va initializa datele membru

    ServiceMessage(RepositoryMessage<Message>& repositoryMessage);
    ///constructorul de copiere

    void addMessage(string name1, string name2, string text);
    ///adauga mesajul cu atributele date in service-ul mesaj

    void removeMessage(string name1, string name2, string text);
    ///sterge mesajul cu atributele date din service-ul mesaj

    int getSize();
    ///returneaza cate elemente de tip mesaj sunt in service-ul mesaj

    Message* getAll();
    ///returneaza adresa mesajelor

    vector<string > showMessagesForAnUser(string name);
    ///memoreaza intr-un vector mesajele unui user dat

    ~ServiceMessage();
    ///destructor

};