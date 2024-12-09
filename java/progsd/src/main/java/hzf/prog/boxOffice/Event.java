package hzf.prog.boxOffice;

public class Event {
    private final Venue venue;
    private final int standardPrice;
    private final int deluxePrice;

    public Event(Venue venue, int standardPrice, int deluxePrice) {
        this.venue = venue;
        this.standardPrice = standardPrice;
        this.deluxePrice = deluxePrice;
    }

    public int reserveSeats(int numSeats, SeatType seatType) {
        if (numSeats <= 0) {
            throw new IllegalArgumentException("numSeats must be greater than 0");
        }
        if (seatType == null) {
            throw new IllegalArgumentException("SeatType must not be null");
        }
        int price = getPriceForType(seatType);
        int rowCount = venue.getNumRows();
        for(int i = 0 ; i < rowCount ; i++) {
            char rowChar = (char)('A'+i);
            int seatsInRow = venue.getNumSeatsInline(rowChar);

            int constantCount = 0;
            int startIdx = -1;

            for(int seatIdx = 1; seatIdx < seatsInRow; seatIdx++) {
                Seat curSeat = venue.getSeat(rowChar, seatIdx);
                if(curSeat.isAvailability() && curSeat.getSeatType()==seatType){
                    constantCount++;
                    if(startIdx == -1) {
                        startIdx = seatIdx;
                    }
                    if(constantCount == numSeats){
                        for(int reserveIdx = startIdx+1; reserveIdx < startIdx+numSeats; reserveIdx++) {
                            Seat s = venue.getSeat(rowChar, reserveIdx);
                            s.setAvailability(false);
                        }
                        return numSeats*price;
                    }
                }
            }
        }
        return -1;
    }

    public void returnSeat (char row, int seatNum){
        Seat seat;
        try {
            seat = venue.getSeat(row, seatNum);
        } catch (IllegalArgumentException e) {
            throw new IllegalArgumentException("ILLEGAL ROW CHAR:" + row + seatNum);
        }
        if (seat.isAvailability()) {
            throw new IllegalArgumentException("SEAT" + row + seatNum + "NOT RESERVED");
        }
        seat.setAvailability(true);
    }
    
    public int getPriceForType(SeatType seatType) {
        if (seatType == null) {
            throw new IllegalArgumentException("SeatType must not be null");
        }
        switch (seatType) {
            case STANDARD:
                return standardPrice;
            case DELUXE:
                return deluxePrice;
            default:
                throw new IllegalArgumentException("未知的座位类型：" + seatType);
        }
    }
}
