import java.util.Locale;
import java.util.ResourceBundle;

public class HelloWorld {
    public static void main(String[] args) {
        // Get the default locale
        Locale currentLocale = Locale.getDefault();

        // Load the resource bundle
        ResourceBundle messages = ResourceBundle.getBundle("Messages", currentLocale);

        // Get the greeting message
        String greeting = messages.getString("greeting");

        System.out.println(greeting);
    }
}
