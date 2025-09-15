package com.example.app;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

class MainTest {
    @Test
    void testGetGreeting() {
        assertEquals("Hello, World!", Main.getGreeting());
    }
}
