import Models.User;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Main {
    public static void main(String[] args) throws JsonProcessingException {
        ObjectMapper objectMapper = new ObjectMapper();
        String userJson = "{\"name\":\"John\",\"age\":21}";
        User userObject = objectMapper.readValue(userJson, User.class);
        System.out.println(userObject.getName() + ", " + userObject.getAge());
    }
}