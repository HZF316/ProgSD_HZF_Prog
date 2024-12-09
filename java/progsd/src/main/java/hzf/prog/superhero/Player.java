package hzf.prog.superhero;

import java.util.HashSet;
import java.util.Set;
import java.util.concurrent.Phaser;

public class Player {
    private final Set<GameCharacter> ownedCharacters;


    public Player(Set<GameCharacter> ownedCharacters) {
        this.ownedCharacters = new HashSet<>(ownedCharacters);
    }
    public void addCharacter(GameCharacter character) {
        ownedCharacters.add(character);
    }
    public Set<GameCharacter> getOwnedCharacters() {
        return ownedCharacters;
    }

    public Set<GameCharacter> chooseCharacters(Power... neededPowers) {
        if (neededPowers == null || neededPowers.length == 0) {
            return new HashSet<>();
        }
        Set<Power> required = new HashSet<>();
        for (Power power : neededPowers) {
            if (power != null) {
                required.add(power);
            }
        }
       //贪心，因为不需要选出所有可能，不需要使用回溯
        Set<GameCharacter> chosen = new HashSet<>();
        //单次遍历角色，能力满足一项就选
        for (GameCharacter gc : ownedCharacters) {
            Set<Power> powers = gc.getPowers();
            // 找出角色是否有匹配的能力
            Set<Power> contribution = new HashSet<>(powers);
            contribution.retainAll(required);
            if (!contribution.isEmpty()) {
                chosen.add(gc);
                required.removeAll(contribution);
                if (required.isEmpty()) {
                    return chosen;
                }
            }
        }
        return null;
    }
}