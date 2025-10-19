package terranews.example.terranews;

import java.util.ArrayList;
import java.util.List;

public record ArticleDto(
        long id,
        String title,
        String source,
        String image,
        long left,
        long center,
        long right,
        long clusterId,
        List<String> leftSources,
        List<String> centerSources,
        List<String> rightSources
) {
    public ArticleDto(long id, String title, String source, String image, long left, long center, long right, long clusterId) {
        this(id, title, source, image, left, center, right, clusterId, new ArrayList<>(), new ArrayList<>(), new ArrayList<>());
    }
}