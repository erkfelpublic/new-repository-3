package com.example.helloworld;

import java.util.stream.Collectors;
import java.util.stream.Stream;

public class HelloWorldMessageProvider implements MessageProvider {

    @Override
    public String getMessage() {
        // An overly complex way to get "Hello, World!"
        String hello = Stream.of("H", "e", "l", "l", "o")
                .collect(Collectors.joining());
        String world = Stream.of("W", "o", "r", "l", "d", "!")
                .collect(Collectors.joining());

        return new StringBuilder()
                .append(hello)
                .append(", ")
                .append(world)
                .toString();
    }
}
