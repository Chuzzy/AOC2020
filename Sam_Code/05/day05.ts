import { readFile } from "fs";
readFile("05/input.txt", (err, data) => {
    if (err) throw err;
    const input = data.toString().split("\r\n");

    const binarySearch = (lo: number, hi: number, instructions: string): number => {
        const mid = (lo + hi) / 2;
        if (instructions === "") 
            return lo;
        
        switch (instructions[0]) {
            case "F":
            case "L":
                return binarySearch(lo, mid, instructions.substr(1));
            case "B":
            case "R":
                return binarySearch(mid, hi, instructions.substr(1));
            default:
                throw new Error(`Unknown instruction ${instructions[0]}`);
        }
    }

    const seats = input.map((line: string): number => {
        const row = binarySearch(0, 128, line.substr(0, 7));
        const col = binarySearch(0, 8, line.substr(7));

        if (row !== Math.floor(row))
            throw new Error(`Got a decmial value for row: ${row}`);

        if (col !== Math.floor(col)) 
            throw new Error(`Got a decimal value for col: ${col}`);
            
        return row * 8 + col;
    }).sort((a, b) => a - b);

    const mySeatIndex = seats.findIndex((id, i) => {
        return id >= 8 && id <= 8 * 128 && seats[i + 1] !== id + 1;
    });

    console.log(`The maximum is ${Math.max(...seats)}`);
    console.log(`My seat ID is ${seats[mySeatIndex] + 1}`);
    
});
