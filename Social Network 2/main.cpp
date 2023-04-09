#include <iostream>
#include "Repository/RepositoryUser.h"
#include "Domain/User.h"
#include "Service/ServiceUser.h"
#include "UI/Ui.h"
#include "UI/Ui.cpp"
#include "Service/ServiceUser.cpp"
#include "Tests/Tests.h"

using namespace std;


int main() {

    runAllTests();

    RepositoryUser<User> repositoryUser;
    RepositoryFriendship<Friendship> repositoryFriendship;
    RepositoryMessage<Message> repositoryMessage;

    ServiceUser serviceUser(repositoryUser);
    ServiceFriendship serviceFriendship(repositoryFriendship);
    ServiceMessage serviceMessage(repositoryMessage);

    Ui ui(serviceUser, serviceFriendship, serviceMessage);
//    ui.addEntityes();
//    ui.showMenu();

    return 0;
}
