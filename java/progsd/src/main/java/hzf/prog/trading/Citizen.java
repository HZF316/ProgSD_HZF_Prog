package hzf.prog.trading;

import java.util.Map;

public class Citizen {
    private int gems;
    private Map<Goods, Integer> inventory;

    public Citizen(int gems, Map<Goods, Integer> inventory) {
        this.gems = gems;
        this.inventory = inventory;
    }
    public int getGems() {
        return gems;
    }
    public int getAmount(Goods goods) {
        return inventory.get(goods);
    }
    public boolean executeTrade (Trade trade){
        int requiredGems = trade.getGems();
        if(requiredGems > gems){
            return false;
        }
        this.gems -= requiredGems;
        Goods goods = trade.getGoods();
        int tradeAmount = trade.getAmount();
        int currentAmount = getAmount(goods);
        inventory.put(goods, currentAmount + tradeAmount);
        return true;
    }

}
