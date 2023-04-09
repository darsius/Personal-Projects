package socialnetwork;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;
import socialnetwork.domain.User;
import socialnetwork.domain.validators.FriendRequestValidator;
import socialnetwork.domain.validators.FriendshipValidator;
import socialnetwork.domain.validators.UserValidator;
import socialnetwork.repository.FriendRequestRepository;
import socialnetwork.repository.FriendshipRepository;
import socialnetwork.repository.UserRepository;
import socialnetwork.service.Service;

import java.io.IOException;
import java.sql.*;

public class LogInController {

    @FXML
    private TextField username;

    @FXML
    private TextField lastname;

    @FXML
    private TextField firstname;

    @FXML
    private PasswordField password;

    @FXML
    private Button btn_logIn;
    @FXML
    private Button btn_signUp;


    @FXML
    private Hyperlink create_acc;

    @FXML
    private Button btn_exit;

    private Service service;
    private Connection connection;
    private PreparedStatement preparedStatement;
    private ResultSet resultSet;

    public void exit(){
        System.exit(0);
    }

    public void initialize() {
        try{
            connection = DriverManager.getConnection("jdbc:postgresql://localhost:5432/socialnetwork5", "postgress", "6162");
            UserRepository userRepository = new UserRepository(connection, new UserValidator());
            FriendRequestRepository friendRequestRepository = new FriendRequestRepository(connection, new FriendRequestValidator());
            FriendshipRepository friendshipRepository = new FriendshipRepository(connection, new FriendshipValidator());
            service = new Service(userRepository, friendshipRepository, friendRequestRepository);

        }catch (SQLException e) {
            e.printStackTrace();
        }

    }

    public void setService(Service service){
        this.service = service;
    }

    public void logIn(ActionEvent actionEvent) throws  IOException{
        String usernameText = username.getText();
        String passwordText = password.getText();

        User user = service.findOneUserByUsername(usernameText);

        if (user != null && user.getPassword().equals(passwordText)) {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("views/feed.fxml"));
            Parent root = loader.load();
            FeedController feedController = loader.getController();
            Scene scene = new Scene(root);

            Stage stage = (Stage) ((Node) actionEvent.getSource()).getScene().getWindow();
            feedController.setLoggedUser(user);
            feedController.setService(service);
            stage.setScene(scene);
            stage.show();
        }
        else
            MessageAlert.showErrorMessage(null, "wrong credentials");
    }

    public void signUp(ActionEvent actionEvent) throws  IOException{
        FXMLLoader loader = new FXMLLoader(getClass().getResource("views/signUp.fxml"));
        Parent root = loader.load();
        SignUpController signUpController = loader.getController();
        signUpController.setService(service);
        Stage stage = (Stage) ((Node) actionEvent.getSource()).getScene().getWindow();

//        Stage stage = (Stage) btn_signUp.getScene().getWindow();
        stage.setScene(new Scene(root));
        stage.show();
    }


}
