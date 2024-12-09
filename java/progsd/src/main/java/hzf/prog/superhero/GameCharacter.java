package hzf.prog.superhero;

import java.util.Objects;
import java.util.Set;

public final class GameCharacter {
    private final String name;
    private final int cost;
    private final Set<Power> powers;

    public GameCharacter(String name, int cost, Set<Power> powers) {
        this.name = name;
        this.cost = cost;
        this.powers = powers;
    }
    public String getName() {
        return name;
    }
    public int getCost() {
        return cost;
    }
    public Set<Power> getPowers() {
        return powers;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof GameCharacter)) return false;
        GameCharacter that = (GameCharacter) o;
        return cost==that.cost && Objects.equals(name,that.name) && Objects.equals(powers,that.powers);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, cost, powers);
    }

    @Override
    public String toString() {
        return "GameCharacter{" +
                "name='" + name + '\'' +
                ", cost=" + cost +
                ", powers=" + powers +
                '}';
    }


}
