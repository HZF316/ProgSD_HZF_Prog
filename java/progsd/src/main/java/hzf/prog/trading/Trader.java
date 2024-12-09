package hzf.prog.trading;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Trader {
    private final List<Trade> trades;
    private final Random random;

    public Trader() {
        this.trades = new ArrayList<>();
        this.random = new Random();
        // 创建初始的随机Trade
        //addRandomTrade()
    }

    public List<Trade> getTrades() {
        return trades;
    }

    public void addRandomTrade(){
        int gems = 1 + random.nextInt(5);
        int amount = 1 + random.nextInt(5);
        Goods[] allGoods = Goods.values();
        Goods randomGoods = allGoods[random.nextInt(allGoods.length)];
        Trade newTrade = new Trade(gems, amount, randomGoods);
        trades.add(newTrade);
    }

    @Override
    public String toString() {
        return "Trader{" +
                "trades=" + trades +
                '}';
    }
}
