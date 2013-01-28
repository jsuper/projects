package org.tony.ui.test;

import java.awt.AWTEvent;
import java.awt.BorderLayout;
import java.awt.Component;
import java.awt.Toolkit;
import java.awt.event.AWTEventListener;
import java.awt.event.MouseEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class SwingTest{
    public static void main(String[] args) {
        JPanel mainPanel = new JPanel();
        mainPanel.add(new JButton("button"));
        final JLabel label = new JLabel("label");
        mainPanel.add(label);

        showFrame("", mainPanel);

        Toolkit.getDefaultToolkit().addAWTEventListener(new AWTEventListener() {
            public void eventDispatched(AWTEvent event) {
                if(event instanceof MouseEvent){
                    MouseEvent evt = (MouseEvent)event;
                    if(evt.getID() == MouseEvent.MOUSE_CLICKED){
                        label.setText("mouse clicked at: " + evt.getPoint());
                    }
                }
            }
        }, AWTEvent.MOUSE_EVENT_MASK);
    }

    public static JFrame showFrame(String title, Component component) {
        JFrame frame = new JFrame();
        frame.setTitle(title);
        frame.getContentPane().add(component, BorderLayout.CENTER);
        frame.setSize(900, 700);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        return frame;
    }
}