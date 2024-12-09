package hzf.prog.trading;

public class Trade {
    private final int gems;
    private final int amount;
    private final Goods goods;

    public Trade(int gems, int amount, Goods goods) {
        this.gems = gems;
        this.amount = amount;
        this.goods = goods;
    }
    public int getGems() {
        return gems;
    }
    public int getAmount() {
        return amount;
    }
    public Goods getGoods() {
        return goods;
    }

    @Override
    public int hashCode() {
        int result = Integer.hashCode(gems);
        result = 31 * result + Integer.hashCode(amount);
        result = 31 * result + goods.hashCode();
        return result;
    }

    @Override
    public String toString() {
        String gemWord = (gems==1)? "gem":"gems";
        return gems + " " + gemWord + " for " + amount + " " + goods;
    }

    public void execute(Trader trader, Citizen citizen){
        if (!trader.getTrades().contains(this)) {
            throw new IllegalArgumentException("Trade not in Trader list");
        }
        boolean success = citizen.executeTrade(this);
        if (success) {
            trader.addRandomTrade();
        }
    }
}
