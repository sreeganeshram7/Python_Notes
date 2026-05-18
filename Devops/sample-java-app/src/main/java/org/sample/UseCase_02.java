package org.sample;

import com.fasterxml.jackson.databind.ObjectMapper;
import java.util.Map;

public class UseCase_02  {
    public static void main(String[] args) throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        Map<String, Object> data =
                mapper.readValue("{\"name\":\"Awanish\",\"age\":30}", Map.class);

        System.out.println(data);
    }
}
