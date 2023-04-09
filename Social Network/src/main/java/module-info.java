module sn.main {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires org.kordamp.bootstrapfx.core;
    requires java.sql;

//    requires de.jensd.fx.fontawesomefx.fontawesome;

    opens socialnetwork to javafx.fxml;
    opens socialnetwork.controller to javafx.fxml;

    exports socialnetwork;
    exports socialnetwork.domain;
    exports socialnetwork.controller;
}