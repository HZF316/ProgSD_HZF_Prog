package hzf.prog.boxOffice;

public class Seat {

    // TODO complete this class according to the specification
    private final char row;
    private final int seatNum;
    private final SeatType seatType;
    private boolean availability;


    public Seat(char row, int seatNum, SeatType seatType) {
        // TODO complete this method
        if (row < 'A' || row > 'Z') {
            throw new IllegalArgumentException("行标识无效。行必须是A到Z之间的一个大写字母。");
        }

        // 验证座位号：必须为正数
        if (seatNum <= 0) {
            throw new IllegalArgumentException("座位号无效。座位号必须为正整数。");
        }

        // seatType理应为枚举值，一般无需特别验证，但若需防止null：
        if (seatType == null) {
            throw new IllegalArgumentException("seatType不能为空。");
        }
        this.row = row;
        this.seatNum = seatNum;
        this.seatType = seatType;
        this.availability = true;
    }
    public char getRow() {
        return row;
    }
    public int getSeatNum() {
        return seatNum;
    }
    public SeatType getSeatType() {
        return seatType;
    }
    public boolean isAvailability() {
        return availability;
    }
    public void setAvailability(boolean available) {
        this.availability = available;
    }

    @Override
    public String toString() {
        return "Seat{" +
                "row=" + row +
                ", seatNumber=" + seatNum +
                ", seatType=" + seatType +
                ", availability=" + availability +
                '}';
    }
}