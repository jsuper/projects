package org.tony.dic.ui;

import javafx.application.Application;
import javafx.geometry.HPos;
import javafx.geometry.VPos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class GridPaneDemo extends Application {

	public void start(Stage primaryStage) throws Exception {
		GridPane root = new GridPane() ;
		root.setHgap(10);
		root.setVgap(10);
//		root.setGridLinesVisible(true) ;
		root.setStyle("-fx-background-color:#f0e68c;-fx-padding:1em");
		
		Label label = new Label("This is the demo label") ;
		label.setStyle("-fx-font-size:2em;-fx-font-weight:bold");
		root.getChildren().add(label);
		GridPane.setConstraints(label, 0, 0, 5, 1, HPos.CENTER, VPos.CENTER);
		
		Button button = new Button("Demo Button");
//		button.setStyle("-fx-background-color:#781096;-fx-border-color:#781096;-fx-border-radius:0") ;
		root.getChildren().add(button);
		GridPane.setConstraints(button, 0, 1, 3, 1);
		
		Label label2 = new Label("/ˈkwiəri/") ;
		root.getChildren().add(label2);
		GridPane.setConstraints(label2, 3, 1, 2, 1);
		
		
		primaryStage.setScene(new Scene(root));
		primaryStage.setWidth(500);
		primaryStage.setHeight(400);
		primaryStage.setTitle("Grid panel demo");
		primaryStage.show() ;
	}
	
	public static void main(String[] args) {
		launch(args);
	}

}
