
#pragma once


#include "../Service/ServiceUser.h"
#include "../Service/ServiceMessage.h"
#include "../Service/ServiceFriendship.h"

class Ui {
private:
    ServiceUser serviceUser;
    ServiceMessage serviceMessage;
    ServiceFriendship serviceFriendship;
    void menuUser();
    void menuFriendship();
    void menuMessage();
    void addUser();
    void removeUser();
    void updateUser();
    void searchUser();
    void showAllUsers();
    void addMessage();
    void removeMessage();
    void showAllMessagesForAnUser();
    void showAllMessages();
    void addFriend();
    void removeFriend();
    void showAllFriends();
    void showFriendsForAnUser();

public:
    Ui();
    Ui(ServiceUser& serviceUser, ServiceFriendship& serviceFriendship, ServiceMessage& serviceMessage);
    void addEntityes();
    void showMenu();

    ~Ui();
};
