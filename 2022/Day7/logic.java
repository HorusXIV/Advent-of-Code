import java.io.*;
import java.util.*;

public class logic {

    public static ArrayList<String[]> readInput(String file)
            throws IOException {
            ArrayList<String> listOfStrings = new ArrayList<String>();
            Scanner sc = new Scanner(new FileReader(file)).useDelimiter("\n");
             while (sc.hasNext()) {
                // adding each string to arraylist
                listOfStrings.add(sc.next());
            }
            ArrayList<String[]> input = new ArrayList<String[]> () ;
            for (String string : listOfStrings){
                String[] Line = string.split(" ");
                input.add(Line);
            }

            return input;

    }

    public static Node getStructure(ArrayList<String[]> array, Node rootNode) {
        Node currentNode = rootNode;
        for (String[] eachLine : array) {
            if (eachLine[0].equals("$")) {
                if (eachLine[1].equals("cd")) {
                    if (eachLine[2].equals("/")) {
                        continue;
                    } else if (eachLine[2].equals("..")) {
                        currentNode = currentNode.getParent();
                    } else {
                        Boolean moved = false;
                        for (Node children : currentNode.getChildren()) {
                            if (children.getName().equals(eachLine[2])) {
                                currentNode = children;
                                moved = true;
                            }
                        }
                        if (!moved) {
                            Node node = new Node(eachLine[2], currentNode);
                            currentNode.addChildren(node);
                            currentNode = node;
                        }
                    }
                } else {
                    continue;
                }
            } else if (eachLine[0].equals("dir")) {
                Node node = new Node(eachLine[1], currentNode);
                currentNode.addChildren(node);
            } else {
                currentNode.addFiles(Integer.parseInt(eachLine[0]));
            }
        }

        return rootNode;

    }

    public static ArrayList<Node> FolderList(Node rootNode) {
        ArrayList<Node> stack = new ArrayList<Node>();
        ArrayList<Node> allFolders = new ArrayList<Node>();

        stack.add(rootNode);
        allFolders.add(rootNode);

        while (!stack.isEmpty()) {
            ArrayList<Node> tempList = new ArrayList<Node>();
            for (Node n : stack) {
                for (Node c : n.getChildren()) {
                    if (!stack.contains(c)) {
                        tempList.add(c);
                        allFolders.add(c);
                    }
                }
            }
            stack.addAll(tempList);
            stack.remove(0);
        }

        return allFolders;
    }
}
