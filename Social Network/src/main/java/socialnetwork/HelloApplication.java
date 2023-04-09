package socialnetwork;


import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import socialnetwork.Tests.Tests;
import socialnetwork.domain.validators.FriendRequestValidator;
import socialnetwork.domain.validators.FriendshipValidator;
import socialnetwork.domain.validators.UserValidator;
import socialnetwork.repository.FriendRequestRepository;
import socialnetwork.repository.FriendshipRepository;
import socialnetwork.repository.UserRepository;
import socialnetwork.service.Service;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Objects;


public class HelloApplication extends Application {

    public static void main(String[] args){
//        Tests tests = new Tests();
//        tests.testAll();
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) throws IOException, SQLException {

        String username="postgres";
        String password="6162";
        String url="jdbc:postgresql://localhost:5432/socialnetwork5";

        Connection connection = DriverManager.getConnection(url, username, password);
        UserRepository userRepository = new UserRepository(connection, new UserValidator());
        FriendRequestRepository friendRequestRepository = new FriendRequestRepository(connection, new FriendRequestValidator());
        FriendshipRepository friendshipRepository = new FriendshipRepository(connection, new FriendshipValidator());
        Service service = new Service(userRepository, friendshipRepository, friendRequestRepository);

        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("views/logIn.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 400, 500);
        LogInController logInController = fxmlLoader.getController();
        logInController.setService(service);
        primaryStage.setTitle("Hello");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

}