package hzf.prog.graphs;

import java.util.Objects;

public class Edge {
    private final Node start;
    private final Node end;
    public Edge(Node start, Node end) {
        this.start = start;
        this.end = end;
    }
    public Node getStart() {
        return start;
    }
    public Node getEnd() {
        return end;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Edge)) return false;
        Edge edge = (Edge) o;
        return Objects.equals(start, edge.start) &&
                Objects.equals(end, edge.end);
    }

    @Override
    public int hashCode() {
        return Objects.hash(start, end);
    }

    @Override
    public String toString() {
        return  "(" + start.getLabel() + ", " + end.getLabel() + ")";
    }
}
