///usr/bin/env jbang "$0" "$@" ; exit $?

//DEPS org.cyclonedx:cyclonedx-core-java:8.0.3
//DEPS org.apache.maven:maven-artifact:3.9.9

import java.io.File;
import java.io.PrintStream;
import java.net.URLDecoder;
import java.nio.file.Files;
import java.nio.file.Path;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.Date;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.stream.Collector;
import java.util.stream.Collectors;

import org.apache.maven.artifact.versioning.ComparableVersion;

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
        if (args[0].endsWith(".sh")) {
            summary(args);
        } else {
            describeSubprojectSBOMs(args);
        }
    }

    public static void summary(String... args) throws Exception {
        String sh = args[0];

        List<String> readme = Files.readAllLines(Path.of("sboms/README.md")).stream().takeWhile(s -> !s.startsWith("##")).collect(Collectors.toList());
        List<String> readmeProjects = readme.stream().filter(s -> s.startsWith("| [")).collect(Collectors.toList());
        Map<String, List<String>> byPmc = new TreeMap<>(Files.readAllLines(Path.of(sh)).stream().filter(s -> s.startsWith("describeReleases")).collect(Collectors.groupingBy(s -> s.split(" ", 3)[1])));

        for(Map.Entry<String,List<String>> e: byPmc.entrySet()) {
            String pmc = e.getKey();
            String pmcName = readmeProjects.stream().filter(s -> s.contains("?" + pmc + ")")).map(s -> s.substring(s.indexOf('[') + 1, s.indexOf(']'))).findFirst().get();
            List<String> projects = e.getValue().stream().map(s -> s.split(" ", 3)[2]).collect(Collectors.toList());

            readme.add("## " + pmcName);
            for(String p: projects) {
                String name;
                String id;
                String pid;
                if (p.startsWith("\"")) {
                    name = p.substring(1, p.lastIndexOf('"'));
                    pid = p.substring(name.length() + 3);
                } else {
                    name = p.substring(0, p.indexOf(' '));
                    pid = p.substring(name.length() + 1);
                }
                id = pid.startsWith("-") ? pmc : pid.split(" ", 2)[0];

                if (projects.size() > 1) {
                    readme.add("### " + name);
                }
                String prefix = "sboms/" + pmc + "/" + id + "-";
                List<String> versions = Arrays.asList(args).stream().filter(s -> s.contains(prefix))
                    .map(s -> s.substring(prefix.length(), s.length() - 3)).filter(s -> Character.isDigit(s.charAt(0)))
                    .map(s -> new ComparableVersion(s)).sorted().map(v -> v.toString())
                    .collect(Collectors.toList());
                for(String v: versions) {
                    String sboms = Files.readAllLines(Path.of(prefix + v + ".md")).get(0);
                    sboms = sboms.substring(sboms.indexOf(':') + 2);
                    readme.add("- " + v + ": [" + (sboms.startsWith("1 ") ? "1 SBOM" : sboms) + "](" + pmc + "/" + id + "-" + v + ".md)");
                }
                readme.add("");
            }
        }

        Files.write(Path.of("sboms/README.md"), readme);
    }

    public static void describeSubprojectSBOMs(String... args) throws Exception {
        String project = args[0];
        String version = args[1];
        out = System.out;
        out.println(project + " " + version + ": " + (args.length - 2) + " SBOMs");
        out.println("=======");
        out.println();
        out.println("| file, spec<br>Serial Number, version| metadata | components<br>by type<br>- libs purl types |");
        out.println("| ----------------------------------- | -------- | ------------------------------------------ |");

        int i = 0;
        for(String path: args) {
            if (i++ < 2) continue;
            String name = path.substring(path.lastIndexOf('/') + 1);
            //name = name.substring(0, name.indexOf("-cyclonedx."));
            System.err.println("Analyzing " + name);
            String extension = name.substring(name.lastIndexOf('.') + 1);
            name = name.substring(0, name.lastIndexOf('.'));

            Date now = new Date();
            Bom bom = readSBOM(path);
            Metadata m = bom.getMetadata();
            if (m != null && m.getTimestamp().after(now)) {
                m.setTimestamp(null); // deserialized init timestamp even if not defined by teh SBOM
            }

            out.print("| **[" + name + "](" + path + ")**<br>" + extension + " ");
            summarize(bom);
        }

        out.close();
    }

    private static Bom readSBOM(String path) throws Exception {
        if (path.endsWith(".json")) {
            JsonParser parser = new JsonParser();
            return parser.parse(new File(path));
        }
        XmlParser parser = new XmlParser();
        return parser.parse(new File(path));
}

    private static void describeMetadata(Metadata meta) throws Exception {
        if (meta == null) {
            out.print(" ");
            return;
        }
        out.print("**" + meta.getComponent().getPurl().substring(4) + "**");
        out.print("<br>type: " + meta.getComponent().getType());
        out.print("<br>timestamp: " + ((meta.getTimestamp() == null) ? "" : DF.format(meta.getTimestamp())));
        if (meta.getTools() != null) {
            out.print("<br>tool: " + meta.getTools().get(0).getName() + " " + meta.getTools().get(0).getVersion());
        } else if (meta.getToolChoice() != null) {
            out.print("<br>tool: " + meta.getToolChoice().getComponents().get(0).getName() + " " + meta.getToolChoice().getComponents().get(0).getVersion());
        }
    }

    private static void summarize(Bom bom) throws Exception {
        if (bom.getBomFormat() == null) {
            out.print(bom.getSpecVersion());
        } else {
            out.print(bom.getBomFormat() + " " + bom.getSpecVersion());
        }
        if (bom.getSerialNumber() != null) {
            out.print("<br>" + bom.getSerialNumber());
            out.print("<br>version: " + bom.getVersion());
        }
        out.print(" | ");
        describeMetadata(bom.getMetadata());
        if (bom.getComponents() == null) {
            out.print(" | 0");
        } else {
            out.print(" | " + bom.getComponents().size());
            print(bom.getComponents().stream().collect(Collectors.groupingBy(c -> c.getType().getTypeName(), Collectors.counting())), "");
            print(bom.getComponents().stream().filter(c -> Component.Type.LIBRARY.equals(c.getType()))
                    .collect(Collectors.groupingBy(c -> extractPurlGroup(c.getPurl()), Collectors.counting())), "- ");
        }
        //out.print("<br>" + ((bom.getDependencies() == null) ? "**NO** " : "") + "deps tree");
        out.println(" |");
    }

    private static void print(Object o, String prefix) {
        out.print("<br>" + prefix + o.toString().replace('{', '`').replace('}', ' ').replace(", ", "<br>" + prefix + "`")
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
