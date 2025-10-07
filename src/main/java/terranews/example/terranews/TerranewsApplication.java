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


@RestController
@SpringBootApplication
public class TerranewsApplication {
    @Autowired
    private ArticleRepository articleRepository;

    public static void main(String[] args) {
		SpringApplication.run(TerranewsApplication.class, args);
	}

    @RequestMapping("/")
    String home() {
        return "Hello World!";
    }
    @RequestMapping("articles")
    public @ResponseBody Iterable<Article> articles() {
        return articleRepository.findAll();
    }
    @RequestMapping("/add")
    String add() {
        Article article = new Article();

        // Ustawiamy pola za pomocą setterów
        article.setTitle("Rząd ogłasza nowy program wsparcia dla studentów");
        article.setContent("Ministerstwo Edukacji wprowadza nowy program stypendialny mający na celu zwiększenie dostępności edukacji wyższej.");
        article.setSource("TVN24");
        article.setDate(LocalDateTime.of(2025, 10, 6, 8, 30, 0));

        articleRepository.save(article);
        System.out.println("dodano");
        return "Hello World!";
    }

}
