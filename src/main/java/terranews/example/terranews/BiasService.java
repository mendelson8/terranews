package terranews.example.terranews;

import org.springframework.stereotype.Service;

import java.util.Map;

@Service
public class BiasService {
    private static final Map<String,String> bias_map = Map.ofEntries(
            // Lewica
            Map.entry("krytykapolityczna.pl", "Lewica"),
            Map.entry("wyborcza.pl", "Lewica"),
            Map.entry("tokfm.pl", "Lewica"),
            Map.entry("tvn24.pl", "Lewica"),
            Map.entry("oko.press", "Lewica"),

            // Prawica
            Map.entry("wgospodarce.pl", "Prawica"),
            Map.entry("telewizjarepublika.pl", "Prawica"),
            Map.entry("tvp.info", "Prawica"),
            Map.entry("wiadomosci.tvp.pl", "Prawica"),
            Map.entry("nczas.com", "Prawica"),
            Map.entry("wpolityce.pl", "Prawica"),
            Map.entry("dorzeczy.pl", "Prawica"),
            Map.entry("gosc.pl", "Prawica"),
            Map.entry("naszdziennik.pl", "Prawica"),

            // Centrum
            Map.entry("rp.pl", "Centrum"),
            Map.entry("onet.pl", "Centrum"),
            Map.entry("polsatnews.pl", "Centrum"),
            Map.entry("interia.pl", "Centrum"),
            Map.entry("forbes.pl", "Centrum"),
            Map.entry("gazetaprawna.pl", "Centrum")
    );
    public String getBias(String sourceUrl){
        sourceUrl = sourceUrl.split("/")[2];
        return bias_map.getOrDefault(sourceUrl,"Centrum");
    }
}
