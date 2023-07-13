// Problem 705: Design HashSet

/**
 * Constraints:
 *
 * 1) 0 <= key <= 10^6
 * 2) At most 10^4 calls will be made to add, remove, and contains
 *
 */

import java.util.HashMap;

class MyHashSet<T> {

    private HashMap<T,Integer> map;

    public MyHashSet() {
        map = new HashMap<>();
    }

    public void add(T key) {
        map.put(key, null);
    }

    public void remove(T key) {
        map.remove(key);
    }

    public boolean contains(T key) {
        return map.containsKey(key);
    }

    public int size() {
        return map.size();
    }
}
