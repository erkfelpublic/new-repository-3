import java.util.Locale;

public class HelloWorld {
    public static void main(String[] args) {
        // Get the default locale
        Locale currentLocale = Locale.getDefault();

        // Create a Greeter for the current locale
        Greeter greeter = new Greeter(currentLocale);

        // Get and print the greeting
        System.out.println(greeter.getGreeting());
    }
}
