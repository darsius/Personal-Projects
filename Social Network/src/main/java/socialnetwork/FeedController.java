package socialnetwork;

import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import socialnetwork.domain.FriendRequest;
import socialnetwork.domain.Friendship;
import socialnetwork.domain.User;
import socialnetwork.service.Service;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.sql.Date;
import java.util.List;
import java.util.Objects;



public class FeedController {
    @FXML
    Button btn_log_out;
    @FXML
    Button btn_add_friend;
    @FXML
    Button btn_accept;
    @FXML
    Button btn_decline;
    @FXML
    Button btn_handleProfileImg;
    @FXML
    TextField tf_search_user;
    @FXML
    Label lb_username;
    @FXML
    ImageView img_profile;
//    @FXML
//    TableView<Friendship> tb_friends;
//    @FXML
//    TableColumn<Friendship, String> cl_tb_friends;
    @FXML
    TableView<User> tb_friends;
    @FXML
    TableColumn<User, String> cl_tb_friends;
    @FXML
    TableView<FriendRequest> tb_friend_requests;
    @FXML
    TableColumn<FriendRequest, String> cl_tb_friend_requests;
    private User loggedUser;

    private Service service;


    public void initialize() {
    try
    {
//        showFriends()?;

//        setLoggedUser(loggedUser);
//        System.out.println(loggedUser.getUsername());


//        updateFriendshipsTable();

    }catch(
    Exception e)

    {
        throw new RuntimeException(e);
    }

}

    public void setLoggedUser(User user) {
        this.loggedUser = user;
        displayUsername();
    }

    public void setService(Service service) {
        this.service = service;
        showFriends();
        showFriendRequests();
        updateFriendRequestTable();
//        updateFriendRequestTable();
    }

    public void goToLogOut(ActionEvent actionEvent) throws IOException{

        FXMLLoader loader = new FXMLLoader(getClass().getResource("views/logIn.fxml"));
        Parent root = loader.load();
        LogInController logInController = loader.getController();
        logInController.setService(service);
        Stage stage = (Stage) ((Node) actionEvent.getSource()).getScene().getWindow();

        stage.setScene(new Scene(root));
        stage.show();
    }

    public void exit(){
        System.exit(0);
    }

    public void displayUsername(){
        lb_username.setText(loggedUser.getUsername());
    }

//    public void searchUser(){
//        tf_search_user.textProperty().addListener((observable, oldValue, newValue) -> {
//            String searchText = newValue;
//            List<User> users = service.searchUser(searchText,loggedUser.getId());
//            ObservableList<User> usersObservable = FXCollections.observableArrayList(users);
//            tf_search_user.setText(usersObservable.toString());
//        });
//    }

    public void searchUser() {
        try{
            if (Objects.equals(tf_search_user.getText(), ""))
            {
                MessageAlert.showErrorMessage(null, "Please fill the searching from! ");
                return;
            }
            User user1 = service.findOneUserByUsername(tf_search_user.getText());

            if (user1 != null) {
                if (user1.equals(loggedUser)){
                    MessageAlert.showErrorMessage(null, "You can't send a friend request to yourself! ");
                    return;
                }
                if (sendFriendRequest()) {
                    MessageAlert.showMessage(null, Alert.AlertType.CONFIRMATION, "", "The friend request has been sent");
                }
            } else
                MessageAlert.showErrorMessage(null, "the user you are trying to search is not existing! ");

        }catch(Exception e)
            {
                throw new RuntimeException(e);
            }
    }

    public void updateFriendRequestTable(){
        List<FriendRequest> friendRequests = service.getFriendRequests(loggedUser.getId());
        tb_friend_requests.setItems(FXCollections.observableList(friendRequests));
    }

//    public void updateFriendsTable(){
//        List<Friendship> friendships = service.getFriendships(loggedUser.getId());
//        tb_friends.setItems(FXCollections.observableList(friendships));
//    }
    public void showUsers(){
        List<User> users = service.findAllExceptYou(loggedUser.getId());
        ObservableList<User> userData = FXCollections.observableList(users);



        TableColumn<User, String> friendsColumn = new TableColumn<>("username");
        friendsColumn.setCellValueFactory(new PropertyValueFactory<>("username"));

        tb_friends.getColumns().setAll(friendsColumn);
        tb_friends.setItems(userData);
    }

    public void showFriends(){
        List<User> friends = service.getFriends(loggedUser.getId());
        ObservableList<User> friendsData = FXCollections.observableList(friends);

        TableColumn<User, String> friendsColumn = new TableColumn<>("Friends");
        friendsColumn.setCellValueFactory(new PropertyValueFactory<>("username"));

        tb_friends.getColumns().setAll(friendsColumn);
        tb_friends.setItems(friendsData);

    }

    public void showFriendRequests(){

        List<FriendRequest> friendRequests = service.getFriendRequests(loggedUser.getId());
        ObservableList<FriendRequest> friendRequestsData = FXCollections.observableList(friendRequests);

        if (friendRequests.size() == 0){
            btn_accept.setVisible(false);
            btn_decline.setVisible(false);
            tb_friend_requests.setPlaceholder(new Label("No friend requests"));
        }

        TableColumn<FriendRequest, String> friendRequestUsernameColumn = new TableColumn<>("Friend Requests");
        friendRequestUsernameColumn.setCellValueFactory(request -> {
            Long senderId = request.getValue().getReceiverId().equals(loggedUser.getId()) ? request.getValue().getSenderId() : request.getValue().getReceiverId();
            User friend = service.findOneUser(senderId);
            return new SimpleStringProperty(friend.getUsername() + " has sent you a friend request on ");
        });


        TableColumn<FriendRequest, Date> friendRequestDateColumn = new TableColumn<>("date");
        friendRequestDateColumn.setCellValueFactory(new PropertyValueFactory<>("date"));

        tb_friend_requests.setItems(friendRequestsData);
        tb_friend_requests.getColumns().setAll(friendRequestUsernameColumn, friendRequestDateColumn);

    }

    public boolean sendFriendRequest(){
        User user = service.findOneUserByUsername(tf_search_user.getText());
        Date date = Date.valueOf(java.time.LocalDate.now());
        FriendRequest friendRequest = new FriendRequest(loggedUser.getId(), user.getId(), date);

        //check if friendship already exists
        List<Friendship> friendships = service.getFriendships(loggedUser.getId());
        for (Friendship friendship : friendships)
            if (Objects.equals(friendship.getUtilizator2(), user.getId()) || Objects.equals(friendship.getUtilizator1(), user.getId())) {
                MessageAlert.showErrorMessage(null, "You are already friend with " + user.getUsername());
                return false;
        }

//        check if friendRequest is already sent
        List<FriendRequest> friendRequests = service.getFriendRequests(user.getId());
        for ( FriendRequest request : friendRequests)
            if (Objects.equals(request.getSenderId(), friendRequest.getSenderId()) && Objects.equals(request.getReceiverId(), friendRequest.getReceiverId())){
                MessageAlert.showErrorMessage(null, "The friend request is already sent! ");
                return false;
            }

        //check if user 2 sent already a friend request to user1
        List<FriendRequest> friendRequests2 = service.getFriendRequests(loggedUser.getId());
        for ( FriendRequest request : friendRequests2)
            if (Objects.equals(request.getSenderId(), friendRequest.getReceiverId()) || Objects.equals(friendRequest.getReceiverId(), friendRequest.getSenderId())){
                MessageAlert.showErrorMessage(null, "User " + user.getUsername() + " already sent you a friend request! ");
                return false;
            }

        service.addFriendRequest(friendRequest);
        return true;
    }

    public void acceptFriendRequest(){
        FriendRequest friendRequest = tb_friend_requests.getSelectionModel().getSelectedItem();


//        List<FriendRequest> friendRequests = service.getFriendRequests(loggedUser.getId());
//        for (FriendRequest f : friendRequests)
//            System.out.println(f.getId() + " " + f.getSenderId() + " " + f.getDate());
//        System.out.println("----------------------");

        if (friendRequest != null) {
            Friendship friendship= new Friendship(friendRequest.getSenderId(), friendRequest.getReceiverId(), (Date) friendRequest.getDate());
            service.addFriendship(friendship);
            System.out.println("Prietenia creata este " + friendship.getUtilizator1() + " " + friendship.getUtilizator2());
            service.deleteFriendRequest(friendRequest.getReceiverId());
            updateFriendRequestTable();
            updateFriendsTable();
        }
    }

    public void updateFriendsTable(){
        List<User> friends = service.getFriends(loggedUser.getId());
//        System.out.println(friends.size());

        List<Friendship> friendships = service.getFriendships(loggedUser.getId());
        for ( Friendship f : friendships)
            System.out.println(f.getUtilizator1() + " " + f.getUtilizator2());

        tb_friends.setItems(FXCollections.observableList(friends));
    }

    public void rejectFriendRequest(){
        FriendRequest friendRequest = tb_friend_requests.getSelectionModel().getSelectedItem();
        if (friendRequest != null) {
            service.deleteFriendRequest(friendRequest.getReceiverId());
            updateFriendRequestTable();
        }
    }

    public void handleProfileImage(ActionEvent actionEvent) throws FileNotFoundException {
        FileChooser fileChooser = new FileChooser();
        fileChooser.getExtensionFilters().addAll(new FileChooser.ExtensionFilter("Images", "*.jpg"));

        Stage stage = (Stage) ((Node) actionEvent.getSource()).getScene().getWindow();
        File file = fileChooser.showOpenDialog(stage);
        if (file != null) {
            Image image = new Image(new FileInputStream(file));
            img_profile.setImage(image);
        }
    }


}



