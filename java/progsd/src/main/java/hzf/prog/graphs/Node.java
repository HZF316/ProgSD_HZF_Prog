package hzf.prog.graphs;

import java.util.ArrayList;
import java.util.List;

public class Node {
    private final int label;
    private final List<Node> neighbours;

    public Node(int label) {
        this.label = label;
        this.neighbours = new ArrayList<>();
    }

    public void addNeighbour (Node node){
        neighbours.add(node);
    }
    public List<Node> getNeighbours(){
        return neighbours;
    }
    public int getLabel() {
        return label;
    }

    @Override
    public String toString() {
        return String.valueOf(label);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Node)) return false;
        Node node = (Node) o;
        return label == node.label;
    }

    @Override
    public int hashCode() {
        return Integer.hashCode(label);
    }
}
