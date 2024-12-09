package hzf.prog.boxOffice;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Venue {
//    在这个例子中set不如数组灵活
//    private Set<Seat> seats;
//    public Set<Seat> constructSeats(String spec) {
//        if (spec == null || spec.isEmpty()) {
//            return new HashSet<>();
//        }
//        String[] lines = spec.split("\n");
//        if (lines.length < 2 || lines.length>27) {
//            throw new IllegalArgumentException("Illegal Spec");
//        }
//        int m = Integer.parseInt(lines[0]);
//        for(int i = 1 ; i < lines.length ; i++) {
//            if (lines[i].isEmpty()) {
//                throw new IllegalArgumentException("Illegal");
//            }
//            String[] seatTypes = lines[i].split("\\s");
//            for (int j = 0 ; j < seatTypes.length ; j++) {
//                if(seatTypes[j]=="S") {
//                    Seat seat = new Seat((char)('A' + i),j+1,SeatType.STANDARD);
//                    seats.add(seat);
//                }else{
//                    Seat seat = new Seat((char)('A' + i),j+1,SeatType.DELUXE);
//                    seats.add(seat);
//                }
//            }
//
//        }
//        return seats;
//    }
    private final Seat[][] seats;
    private final int numRows;

    public Venue(String config) {
        String[] lines = config.split("\n");
        if (lines.length < 2) {
            throw new IllegalArgumentException("lack of data");
        }
        this.numRows = Integer.parseInt(lines[0]);
        if (numRows < 1 || numRows > 26) {
            throw new IllegalArgumentException("Too much or too less lines");
        }
        this.seats = new Seat[numRows][];
        for (int i = 0; i < numRows; i++) {
            String rowLine = lines[i + 1];
            if (rowLine.isEmpty()) {
                throw new IllegalArgumentException("line " + (char)('A' + i) + "empty");
            }
            String[] seatTypes = rowLine.split("\\s+");
            seats[i] = new Seat[seatTypes.length];
            char rowChar = (char)('A' + i);
            for (int j = 0; j < seatTypes.length; j++) {
                int seatNumber = j + 1;
                SeatType type = mapSeatType(seatTypes[j]);
                Seat seat = new Seat(rowChar, seatNumber, type);
                seats[i][j] = seat;
            }
        }
    }

    public SeatType mapSeatType(String seatType) {
        switch (seatType.toUpperCase()) {
            case "S":
                return SeatType.STANDARD;
            case "D":
                return SeatType.DELUXE;
            default:
                throw new IllegalArgumentException("USELESS: " + seatType);
        }

    }

    public Seat getSeat(char row, int seatNum){
        if (row < 'A' || row >= 'A' + numRows) {
            throw new IllegalArgumentException("ILLEGAL LINE：" + row + ". LINE SHOULD BE WITH IN A" + (char)('A' + numRows - 1));
        }

        int rowIndex = row - 'A';
        if (seatNum <= 0 || seatNum > seats[rowIndex].length) {
            throw new IllegalArgumentException("ILLEGAL SEATNUMBER：" + seatNum + ". THERE ARE" + seats[rowIndex].length + "SEATS IN THIS LINE");
        }
        return seats[rowIndex][seatNum-1];
    }

    public void printDetails(){
        for (int i = 0; i < numRows; i++) {
            char rowChar = (char)('A' + i);
            System.out.println("Row " + rowChar + ":");
            for (int j = 0; j < seats[i].length; j++) {
                Seat s = seats[i][j];
                String availabilityStr = s.isAvailability() ? "available" : "reserved";
                System.out.println(s.getRow() + "" + s.getSeatNum() + ": " + s.getSeatType() + " (" + availabilityStr + ")");
            }
        }
    }

    public int getNumRows() {
        return numRows;
    }

    public int getNumSeatsInline(char rowChar) {
        int rowIdx = (rowChar - 'A');
        return seats[rowIdx].length;
    }
}
