import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

/**
 * Unit test for the HelloWorld class.
 */
class HelloWorldTest {

    /**
     * Tests the main method of the HelloWorld class.
     * It redirects the standard output, calls the main method, and then asserts that the output is correct.
     */
    @Test
    void main() {
        // Redirect System.out to capture the output
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(outContent));

        // Call the main method
        HelloWorld.main(new String[]{});

        // Restore System.out
        System.setOut(originalOut);

        // Assert the output
        // The expected output should have a newline character at the end, because System.out.println adds one.
        assertEquals("Hello, World!\n", outContent.toString());
    }
}
