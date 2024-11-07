///usr/bin/env jbang "$0" "$@" ; exit $?

//DEPS org.cyclonedx:cyclonedx-core-java:8.0.3

import java.io.File;
import java.io.PrintStream;
import java.net.URLDecoder;
import java.nio.file.Files;
import java.text.SimpleDateFormat;
import java.util.Collections;
import java.util.Comparator;
import java.util.Iterator;
import java.util.List;
import java.util.stream.Collectors;

import org.cyclonedx.BomGeneratorFactory;
import org.cyclonedx.CycloneDxSchema;
import org.cyclonedx.generators.xml.BomXmlGenerator;
import org.cyclonedx.model.Bom;
import org.cyclonedx.model.Component;
import org.cyclonedx.model.Metadata;
import org.cyclonedx.model.Tool;
import org.cyclonedx.parsers.JsonParser;
import org.cyclonedx.parsers.XmlParser;

public class describe_sboms {
    private static PrintStream out;
    private static SimpleDateFormat DF = new SimpleDateFormat("yyyy-MM-dd' 'HH:mm:ss");

    public static void main(String... args) throws Exception {

        out = System.out;
        out.println("Summary of SBOMs");
        out.println("=======");
        out.println();
        out.println("| file | metadata | components | by type | libraries purl types | deps tree |");
        out.println("| ---- | -------- | ---------- | ------- | -------------------- | --------- |");

        int i = 1;
        for(String path: args) {
            String name = path.substring(path.lastIndexOf('/') + 1);
            //name = name.substring(0, name.indexOf("-cyclonedx."));
            System.err.println("Analyzing " + name);

            Bom bom = readJsonSBOM(path);

            out.print("| **[" + name + "](" + path + ")**");
            summarize(bom);
        }

        out.close();
    }

    private static Bom readJsonSBOM(String path) throws Exception {
        if (path.endsWith(".json")) {
            JsonParser parser = new JsonParser();
            return parser.parse(new File(path));
        }
        XmlParser parser = new XmlParser();
        return parser.parse(new File(path));
}

    private static void describeMetadata(Metadata meta) throws Exception {
        out.print("**component**: " + meta.getComponent().getPurl());
        out.print("<br>type: " + meta.getComponent().getType());
        out.print("<br>timestamp: " + DF.format(meta.getTimestamp()));
        if (meta.getTools() != null) {
            out.print("<br>tool: " + meta.getTools().get(0).getName() + " " + meta.getTools().get(0).getVersion());
        } else if (meta.getToolChoice() != null) {
            out.print("<br>tool: " + meta.getToolChoice().getComponents().get(0).getName() + " " + meta.getToolChoice().getComponents().get(0).getVersion());
        }
    }

    private static void summarize(Bom bom) throws Exception {
        out.print("<br>" + bom.getBomFormat() + " " + bom.getSpecVersion());
        out.print("<br>" + bom.getSerialNumber());
        out.print("<br>version: " + bom.getVersion());
        out.print(" | ");
        describeMetadata(bom.getMetadata());
        if (bom.getComponents() == null) {
            out.print(" | 0");
        } else {
            out.print(" | " + bom.getComponents().size());
            print(bom.getComponents().stream().collect(Collectors.groupingBy(c -> c.getType().getTypeName(), Collectors.counting())));
            print(bom.getComponents().stream().filter(c -> Component.Type.LIBRARY.equals(c.getType()))
                    .collect(Collectors.groupingBy(c -> extractPurlGroup(c.getPurl()), Collectors.counting())));
        }
        out.print(" | " + (bom.getDependencies() != null));
        out.println(" |");
    }

    private static void print(Object o) {
        out.print(" | " + o.toString().replace('{', '`').replace('}', ' ').replace(", ", "<br>`")
                .replace("=", "`: "));
    }

    private static String extractPurlGroup(String purl) {
        if (purl.startsWith("pkg:generic/")) {
            int second = purl.indexOf('/', 12);
            return second < 0 ? "generic" : URLDecoder.decode(purl.substring(4, second));
        } else {
            return purl.substring(4, purl.indexOf('/'));
        }
    }
}
