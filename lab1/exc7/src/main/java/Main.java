import Models.User;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Main {
    public static void main(String[] args) throws JsonProcessingException {
        ObjectMapper objectMapper = new ObjectMapper();
        User userObject = new User("John", 21);
        String userJson = objectMapper.writeValueAsString(userObject);
        System.out.println(userJson);
    }
}