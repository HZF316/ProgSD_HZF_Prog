package hzf.prog.graphs;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class GraphExplorer {
    public static Set<Edge> listEdges(Node[] nodes) {
        Set<Edge> edges = new HashSet<>();
        for (Node node : nodes) {
            List<Node> neighbours = node.getNeighbours();
            for (Node neighbour : neighbours) {
                edges.add(new Edge(node, neighbour));
            }
        }
        return edges;
    }

}
