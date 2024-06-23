import java.util.ArrayList;
import java.util.List;

public class Node {
    String name;
    List<Edge>edges;
    public Node (String name){
        this.name = name;
        this.edges = new ArrayList<Edge>();
    }
}
