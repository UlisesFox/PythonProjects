import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class Graph {
    List<Node>nodes;
    Node root;

    public Graph(){
        this.nodes = new ArrayList<>();
        Node a = new Node ("A");
        Node b = new Node ("B");
        Edge ab = new Edge(2, a, b);
        this.nodes.add(a);
        this.nodes.add(b);
        this.root = a;
        Node c = new Node("C");
        Edge ca = new Edge(3, c, a);
        this.nodes.add(c);
        a.edges.add(ab);
        c.edges.add(ca);
    }
    
    public Node recursiveSearchbyDeep(String tgtName, Stack<Node>toEval, Stack<Node>evaluate){
        if(toEval.isEmpty()){
            return null;
        }
        Node root = toEval.pop();
        evaluate.add(root);
        if(root.name.equals(tgtName)){
            return root;
        }
        for(Edge e : root.edges){
            if(!evaluate.contains(e.targer)){
                toEval.push(e.targer);
            }
        }
        return recursiveSearchbyDeep(tgtName, toEval, evaluate);
    }

    public static void main(String[] args) {
        new Graph();
    }
}
