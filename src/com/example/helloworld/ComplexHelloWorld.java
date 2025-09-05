package com.example.helloworld;

import java.lang.reflect.Constructor;

public class ComplexHelloWorld {

    private final MessageProvider messageProvider;
    private final OutputService outputService;

    public ComplexHelloWorld(MessageProvider messageProvider, OutputService outputService) {
        this.messageProvider = messageProvider;
        this.outputService = outputService;
    }

    public void run() {
        outputService.printMessage(messageProvider.getMessage());
    }

    public static void main(String[] args) {
        // Overly complex instantiation using reflection
        try {
            Constructor<HelloWorldMessageProvider> messageProviderConstructor = HelloWorldMessageProvider.class.getConstructor();
            MessageProvider messageProvider = messageProviderConstructor.newInstance();

            Constructor<ConsoleOutputService> outputServiceConstructor = ConsoleOutputService.class.getConstructor();
            OutputService outputService = outputServiceConstructor.newInstance();

            ComplexHelloWorld app = new ComplexHelloWorld(messageProvider, outputService);
            app.run();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
