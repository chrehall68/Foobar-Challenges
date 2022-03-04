import java.util.ArrayList;
import java.util.Objects;
import java.util.HashMap;

class Vector {
    private int x;
    private int y;

    public Vector(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public Vector simplifiesTo() {
        if (x == 0)
            return new Vector(0, (int) Math.signum(y));
        if (y == 0)
            return new Vector((int) Math.signum(x), 0);
        int temp_x = x, temp_y = y;
        for (int i = Math.min(Math.abs(x), Math.abs(y)); i > 0; i--) {
            if (temp_x % i == 0 && temp_y % i == 0) {
                temp_x /= i;
                temp_y /= i;
            }
        }
        return new Vector(temp_x, temp_y);
    }

    @Override
    public boolean equals(Object o) {
        if (o instanceof Vector) {
            Vector temp = (Vector) o;
            return this.x == temp.x && this.y == temp.y;
        }

        return false;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }

    public boolean longerThan(Vector o) {
        return Math.abs(x) >= Math.abs(o.x) && Math.abs(y) >= Math.abs(o.y);
    }

    public boolean shorterThan(Vector o) {
        return Math.abs(x) <= Math.abs(o.x) && Math.abs(y) <= Math.abs(o.y);
    }

    public String toString() {
        return "(" + x + ", " + y + ")";
    }

}

public class BringingAGunToATrainerFight {
    public static int adjust(int x, int min_val, int max_val) {
        while (x < min_val || x > max_val) {
            if (x < min_val) {
                x = Math.abs(x);
            }
            if (x > max_val) {
                // max_val - (x-max_val)
                x = 2 * max_val - x;
            }
        }
        return x;
    }

    public static double adjust(double x, int min_val, int max_val) {
        while (x < min_val || x > max_val) {
            if (x < min_val) {
                x = Math.abs(x);
            }
            if (x > max_val) {
                // max_val - (x-max_val)
                x = 2 * max_val - x;
            }
        }
        return x;
    }

    public static boolean tooFar(int x, int y, int max_length) {
        return Math.pow(x, 2) + Math.pow(y, 2) > Math.pow(max_length, 2);
    }

    public static int solution(int[] dimensions, int[] your_position, int[] trainer_position, int distance) {
        ArrayList<Integer> valid_x = new ArrayList<>();
        ArrayList<Integer> valid_y = new ArrayList<>();
        HashMap<Vector, Vector> valid_map = new HashMap<>();

        // get the shortest vector in each direction that will hit the trainer
        for (int x = -distance; x <= distance; x++)
            if (adjust(x + your_position[0], 0, dimensions[0]) == trainer_position[0])
                valid_x.add(x);
        for (int y = -distance; y <= distance; y++)
            if (adjust(y + your_position[1], 0, dimensions[1]) == trainer_position[1])
                valid_y.add(y);
        for (int x : valid_x) {
            for (int y : valid_y) {
                if (!tooFar(x, y, distance)) {
                    Vector t = new Vector(x, y);
                    Vector simplifies_to = t.simplifiesTo();
                    if (valid_map.containsKey(simplifies_to)) {
                        Vector compare_to = valid_map.get(simplifies_to);
                        if (t.shorterThan(compare_to)) {
                            valid_map.put(simplifies_to, t);
                        }
                    } else {
                        valid_map.put(simplifies_to, t);
                    }
                }
            }
        }

        // get the shortest vector in each direction that will hit you
        valid_x = new ArrayList<>();
        valid_y = new ArrayList<>();
        HashMap<Vector, Vector> invalid_map = new HashMap<>();
        for (int x = -distance; x <= distance; x++)
            if (adjust(x + your_position[0], 0, dimensions[0]) == your_position[0])
                valid_x.add(x);
        for (int y = -distance; y <= distance; y++)
            if (adjust(y + your_position[1], 0, dimensions[1]) == your_position[1])
                valid_y.add(y);
        for (int x : valid_x) {
            for (int y : valid_y) {
                if (!tooFar(x, y, distance)) {
                    Vector t = new Vector(x, y);
                    Vector simplifies_to = t.simplifiesTo();
                    if (invalid_map.containsKey(simplifies_to)) {
                        Vector compare_to = invalid_map.get(simplifies_to);
                        if (t.shorterThan(compare_to)) {
                            invalid_map.put(simplifies_to, t);
                        }
                    } else {
                        invalid_map.put(simplifies_to, t);
                    }
                }
            }
        }

        // for each simplified vector that will hit you, check if there is a vector
        // that goes in the same direction in valid. If there is, make sure that
        // that vector is SHORTER than the one that will hit you. If longer, remove it
        for (Vector simple : invalid_map.keySet()) {
            if (valid_map.containsKey(simple)) {
                Vector invalid_length = invalid_map.get(simple);
                Vector valid_length = valid_map.get(simple);
                if (valid_length.longerThan(invalid_length)) {
                    valid_map.remove(simple);
                }
            }
        }

        System.out.println(valid_map);
        System.out.println();
        System.out.println("invalid" + invalid_map);
        // for (Vector simple : valid_map.values()) System.out.println(simple);

        return valid_map.size();
    }

    public static void main(String[] args) {
        int[] dim = { 3, 2 };
        int[] your_pos = { 1, 1 };
        int[] train_pos = { 2, 1 };
        int max_length = 4;

        int[] dim2 = { 300, 275 };
        int[] your_pos2 = { 150, 150 };
        int[] train_pos2 = { 185, 100 };
        int max_length2 = 500;

        int[] dim3 = { 3, 2 };
        int[] your_pos3 = { 1, 1 };
        int[] train_pos3 = { 2, 1 };
        int max_length3 = 1000;

        int[] dim4 = { 1000, 1000 };
        int[] your_pos4 = { 274, 229 };
        int[] train_pos4 = { 723, 100 };
        int max_length4 = 2000;
        System.out.println(solution(dim, your_pos, train_pos, max_length));
        System.out.println(solution(dim2, your_pos2, train_pos2, max_length2));
        System.out.println(solution(dim3, your_pos3, train_pos3, max_length3));
        System.out.println(solution(dim4, your_pos4, train_pos4, max_length4));
    }
}