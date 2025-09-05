package com.example.helloworld;

public class ConsoleOutputService implements OutputService {

    @Override
    public void printMessage(String message) {
        // A simple implementation, but could be more complex
        // for example by using a logger or a different output stream.
        System.out.println(message);
    }
}
