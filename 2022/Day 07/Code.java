import java.io.*;
import java.util.*;

public class Code {
    public static void main(String[] args)
            throws IOException {
        // Reading input
        ArrayList<String[]> input = logic.readInput("2022\\Day 07\\input.txt");

        // Calculating the Folderstructure starting on /
        Node rootNode = new Node("/", null);
        rootNode = logic.getStructure(input, rootNode);

        // creating 1D picture of the Folderstructure
        ArrayList<Node> allFolders = logic.FolderList(rootNode);

        // solving Part 1
        int sum = 0;
        for (Node x : allFolders) {
            if (x.calcSize() < 100000) {
                sum += x.calcSize();
            }
        }
        System.out.println("Part 1: " + sum);

        // solving Part 2
        int FreeSpace = 70000000 - rootNode.calcSize();
        Node closestFolder = rootNode;
        for (Node folder : allFolders) {
            if ((folder.calcSize() + FreeSpace) > 30000000 && folder.calcSize() < closestFolder.calcSize()) {
                closestFolder = folder;
            }
        }
        System.out.println("Part2: " + closestFolder.calcSize());

    }
}