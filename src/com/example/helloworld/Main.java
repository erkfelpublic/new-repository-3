package com.example.helloworld;

public class Main {
    public static void main(String[] args) {
        MessageProvider provider = GreeterFactory.getMessageProvider();
        MessageRenderer renderer = GreeterFactory.getMessageRenderer();

        String message = provider.getMessage();
        renderer.render(message);
    }
}
