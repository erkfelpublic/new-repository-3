package com.example.helloworld;

public class GreeterFactory {
    public static MessageProvider getMessageProvider() {
        return new HelloWorldMessageProvider();
    }

    public static MessageRenderer getMessageRenderer() {
        return new ConsoleMessageRenderer();
    }
}
