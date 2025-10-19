package terranews.example.terranews;
import org.springframework.data.repository.query.Param;
import terranews.example.terranews.ArticleDto;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ArticleRepository extends JpaRepository<Article, Long> {
    @Query(
            value = """
            SELECT
                a.id         AS id,
                a.title      AS title,
                a.source     AS source,
                a.image      AS image,
                CAST(0 AS BIGINT) AS left,
                CAST(0 AS BIGINT) AS right,
                CAST(0 AS BIGINT) AS center,
                a.cluster_id AS clusterId
            FROM (
                SELECT DISTINCT ON (cluster_id) *
                FROM articles
                WHERE cluster_id IS NOT NULL
                ORDER BY cluster_id, date DESC
            ) a
            """,
            nativeQuery = true
    )
    List<ArticleDto> findAllIds();

    @Query(
            value = """
            SELECT
                a.id         AS id,
                a.title      AS title,
                a.source     AS source,
                a.image      AS image,
                CAST(0 AS BIGINT) AS left,
                CAST(0 AS BIGINT) AS right,
                CAST(0 AS BIGINT) AS center,
                a.cluster_id AS clusterId
            FROM articles a
            WHERE a.cluster_id = :aLong
            """,
            nativeQuery = true
    )
    List<ArticleDto> getArticleByCluster(@Param("aLong") Long aLong);

    @Query(
            value = """
            SELECT
                a.id         AS id,
                a.title      AS title,
                a.source     AS source,
                a.image      AS image,
                CAST(0 AS BIGINT) AS left,
                CAST(0 AS BIGINT) AS right,
                CAST(0 AS BIGINT) AS center,
                a.cluster_id AS clusterId
            FROM articles a
            WHERE a.id= :arid
            """,
            nativeQuery = true
    )
    List<ArticleDto> getArticleDtoById(@Param("arid") Long arid);
}