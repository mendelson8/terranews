package terranews.example.terranews;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class ArticleService {
    @Autowired
    ArticleRepository articleRepository;
    @Autowired
    BiasService biasService;

    public List<ArticleDto> getAllArticlesWithBias(){
        List<ArticleDto> articles = articleRepository.findAllIds();
        List<ArticleDto> result = new ArrayList<>();
        for (ArticleDto article : articles) {
            System.out.println("Processing article id: " + article.clusterId());
            long lewica = 0;
            List<String> lewicowe = new ArrayList<>();
            long centrum = 0;
            List<String> centrowe = new ArrayList<>();
            long prawica = 0;
            List<String> prawicowe = new ArrayList<>();
            List<ArticleDto> subarticles = articleRepository.getArticleByCluster(article.clusterId());
            for (ArticleDto subarticle : subarticles) {
                String bias = biasService.getBias(subarticle.source());
                switch (bias) {
                    case "Lewica":
                        lewica++;
                        lewicowe.add(subarticle.source());
                        break;
                    case "Centrum":
                        centrum++;
                        centrowe.add(subarticle.source());
                        break;
                    case "Prawica":
                        prawica++;
                        prawicowe.add(subarticle.source());
                        break;
                }
            }
            result.add(new ArticleDto(
                    article.id(),
                    article.title(),
                    article.source(),
                    article.image(),
                    lewica,
                    centrum,
                    prawica,
                    article.clusterId(),
                    lewicowe,
                    centrowe,
                    prawicowe
            ));

        }
        return result;
    }

    public List<ArticleDto> getArticleWithBiasWithId(long articleId){
        List<ArticleDto> articles = articleRepository.getArticleDtoById(articleId);
        List<ArticleDto> result = new ArrayList<>();
        for (ArticleDto article : articles) {
            System.out.println("Processing article id: " + article.clusterId());
            long lewica = 0;
            List<String> lewicowe = new ArrayList<>();
            long centrum = 0;
            List<String> centrowe = new ArrayList<>();
            long prawica = 0;
            List<String> prawicowe = new ArrayList<>();
            List<ArticleDto> subarticles = articleRepository.getArticleByCluster(article.clusterId());
            for (ArticleDto subarticle : subarticles) {
                String bias = biasService.getBias(subarticle.source());
                switch (bias) {
                    case "Lewica":
                        lewica++;
                        lewicowe.add(subarticle.source());
                        break;
                    case "Centrum":
                        centrum++;
                        centrowe.add(subarticle.source());
                        break;
                    case "Prawica":
                        prawica++;
                        prawicowe.add(subarticle.source());
                        break;
                }
            }
            result.add(new ArticleDto(
                    article.id(),
                    article.title(),
                    article.source(),
                    article.image(),
                    lewica,
                    centrum,
                    prawica,
                    article.clusterId(),
                    lewicowe,
                    centrowe,
                    prawicowe
            ));

        }
        return result;
    }
}