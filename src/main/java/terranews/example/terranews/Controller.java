package terranews.example.terranews;
import terranews.example.terranews.ArticleDto;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@CrossOrigin
public class Controller {
    @Autowired
    ArticleRepository articleRepository;
    @Autowired
    ArticleService articleService;

    @RequestMapping("/")
    long home() {
        return articleRepository.count();
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

    @RequestMapping("/api/articles")
    public List<ArticleDto> getArticles() {
        return articleService.getAllArticlesWithBias();
    }

    @RequestMapping("/api/articles/{articleId}")
    public List<ArticleDto> getArticle(@PathVariable("articleId") long articleId) {
        return articleService.getArticleWithBiasWithId(articleId);
    }
}

