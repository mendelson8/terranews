package terranews.example.terranews;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;



@SpringBootApplication
public class TerranewsApplication {
    @Autowired
    private ArticleRepository articleRepository;

    public static void main(String[] args) {
		SpringApplication.run(TerranewsApplication.class, args);
	}
}
