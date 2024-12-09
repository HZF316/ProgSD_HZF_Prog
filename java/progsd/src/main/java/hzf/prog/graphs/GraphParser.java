package hzf.prog.graphs;

public class GraphParser {
    public static Node[] parseGraph (String spec){
        if (spec == null || spec.isEmpty()) return null;
        String[] lines = spec.split("\n");
        // parseInt or valueOf
        int m = Integer.parseInt(lines[0].trim());
        int n = Integer.parseInt(lines[1].trim());

        Node[] nodes = new Node[n];

        for (int i = 0; i < n; i++) {
            nodes[i] = new Node(i+1);
        }

        for(int i =2 ; i < 2+m ; i++){
            String line = lines[i].trim();
            if (line.isEmpty()) continue;
            // " "or "\\s"
            String[] parts = line.split("\\s+");
            int from = Integer.parseInt(parts[0]);
            int to = Integer.parseInt(parts[1]);
            nodes[from - 1].addNeighbour(nodes[to - 1]);
        }
        return nodes;
    }

}
