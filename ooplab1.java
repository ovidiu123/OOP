public class Guitar {
    private boolean isMoving;
    private int speed;
    private String color;

    // Constructor to initialize the guitar's state
    public Guitar(boolean isMoving, int speed, String color) {
        this.isMoving = isMoving;
        this.speed = speed;
        this.color = color;
    }

    // Method to print the guitar's state to the console
    public void printState() {
        System.out.println("Guitar State: " + (isMoving ? "Moving" : "Standing"));
        System.out.println("Speed: " + speed + " mph");
        System.out.println("Color: " + color);
    }

    public static void main(String[] args) {
        // Create a Guitar object and print its state
        Guitar myGuitar = new Guitar(true, 30, "Red");
        myGuitar.printState();
    }
}
