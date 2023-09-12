// hello world

public class Guitar {
    boolean isPlaying;
    int speed;
    String color;

    public Guitar(boolean isPlaying, int speed, String color) {
        this.isPlaying = isPlaying;
        this.speed = speed;
        this.color = color;
    }
    public void printState() {
        System.out.println("Guitar State: " + (isPlaying ? "Playing" : "Standing"));
        System.out.println("Speed: " + speed + " bpm");
        System.out.println("Color: " + color);
    }

    public static void main(String[] args) {
       
        Guitar myGuitar = new Guitar(true, 30, "Red");
        myGuitar.printState();
    }
}
