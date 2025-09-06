package com.example.hello;

/**
 * The main class for the Hello World application.
 */
public class Main {
    /**
     * The main entry point for the application.
     * @param args command line arguments (not used)
     */
    public static void main(String[] args) {
        Greeter greeter = new Greeter();
        System.out.println(greeter.getGreeting());
    }
}
