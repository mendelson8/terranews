package terranews.example.terranews;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class Controller {
    @Autowired
    ArticleRepository articleRepository;

    @RequestMapping("/")
    String home() {
        return "Hello World!";
    }

    @RequestMapping("articles")
    public @ResponseBody Iterable<Article> articles() {
        return articleRepository.findAll();
    }

    @PostMapping("/addBatch")
    public String addBatch(@RequestBody List<Article> articles) {
        int i =0;
        for  (Article article : articles) {
            try{
                articleRepository.save(article);
                i++;
            }
            catch(DataIntegrityViolationException e) {
                System.out.println(e.getMessage());
            }
        }
        System.out.println(i);
        return "Articles added";
    }
}
