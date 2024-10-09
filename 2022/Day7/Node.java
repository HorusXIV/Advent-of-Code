import java.util.ArrayList;

public final class Node {
    private final String name;
    private final Node parent;
    private ArrayList<Node> children = new ArrayList<Node>();
    private ArrayList<Integer> files = new ArrayList<Integer>();
        
    public Node(String name, Node parent){
        this.name = name;
        this.parent = parent;
    }

    public String getName() {
        return name;
    }

    public Node getParent() {
        return parent;
    }

    public ArrayList<Node> getChildren() {
        return children;
    }

    public ArrayList<Integer> getFiles() {
        return files;
    }
        
    public void addChildren(Node node){
        this.children.add(node);
    }

    public void addFiles(int size){
        files.add(size);
    }

    public int calcSize(){
        int size = 0;

        if (!files.isEmpty()){
            for (int bites : files){
                size += bites;
            }
        }
        if (!children.isEmpty()){
            for (Node child : children){
                size += child.calcSize();
            }
        }
        
        return size;
    }
 
}
