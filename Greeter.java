import java.util.Locale;
import java.util.ResourceBundle;

public class Greeter {
    private Locale locale;
    private ResourceBundle messages;

    public Greeter(Locale locale) {
        this.locale = locale;
        this.messages = ResourceBundle.getBundle("Messages", this.locale);
    }

    public String getGreeting() {
        return messages.getString("greeting");
    }
}
