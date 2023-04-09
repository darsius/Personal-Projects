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
import org.w3c.dom.Text;
import socialnetwork.domain.User;
import socialnetwork.service.Service;
import socialnetwork.utils.events.Event;
import socialnetwork.utils.observer.Observer;

import java.io.IOException;
import java.sql.*;
import java.util.Objects;
import java.util.UUID;

public class SignUpController implements Observer<Event> {

    @FXML
    private TextField username;

    @FXML
    private TextField lastname;

    @FXML
    private TextField firstname;

    @FXML
    private PasswordField password;

    @FXML
    private Button btn_login;

    @FXML
    private Hyperlink create_acc;

    @FXML
    private Button btn_exit;

    @FXML
    private Text errorField;

    private Service service;
    private Connection connection;
    private PreparedStatement preparedStatement;
    private ResultSet resultSet;

    public void exit(){
        System.exit(0);
    }

    public void initialize(){
        btn_login.setVisible(false);
    }

    public void setService(Service service) {
        this.service = service;
        service.addObserver(this);
    }

    public void signUp(ActionEvent actionEvent) {
        try {
            if (firstname.getText().isEmpty() || lastname.getText().isEmpty() || username.getText().isEmpty() || password.getText().isEmpty()){
                MessageAlert.showErrorMessage(null, "All fields need to be completed!");
                return;
            }
            else {
                User user = service.findOneUserByUsername(username.getText());
                if (user != null) {
                    MessageAlert.showErrorMessage(null, "This username is already used! Try another one instead");
                    return;
                }
            }
            User user = new User();
            Long id = UUID.randomUUID().getMostSignificantBits() & Long.MAX_VALUE;
            user.setId(id);
            user.setFirstName(firstname.getText());
            user.setLastName(lastname.getText());
            user.setUsername(username.getText());
            user.setPassword(password.getText());
            service.addUser(user);
            if (Objects.equals(user.getUsername(), service.findOneUserByUsername(username.getText()).getUsername())){
                MessageAlert.showMessage(null, Alert.AlertType.INFORMATION,"" ,"Your registration has been completed! ");
                btn_login.setVisible(true);
            }
            else
                MessageAlert.showErrorMessage(null, "Oops! Something went wrong");

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public void goToLogIn(ActionEvent actionEvent) throws IOException {

        FXMLLoader loader = new FXMLLoader(getClass().getResource("views/logIn.fxml"));
        Parent root = loader.load();
        LogInController logInController = loader.getController();
        logInController.setService(service);
        Stage stage = (Stage) ((Node) actionEvent.getSource()).getScene().getWindow();

        stage.setScene(new Scene(root));
        stage.show();
    }


    @Override
    public void update(Event event) {

    }
}

// nu merge sa adaug userul in baza de date
// nu merge cand ma intorc la login page sa ma loghez