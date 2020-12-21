import { readFile } from "fs";

readFile("11/input.txt", (err, data) => {
    if (err) throw err;

    const input = data.toString().split("\r\n");
    const width = input[0].length;
    const height = input.length;

    const adjacentCoords = (coords: [number, number]): [number, number][] => {
        const offsets: [number, number][] = [
            [-1, -1],
            [0, -1],
            [1, -1],
            [1, 0],
            [1, 1],
            [0, 1],
            [-1, 1],
            [-1, 0]
        ];

        return offsets.map(
            (offset: [number, number]): [number, number] =>
                [coords[0] + offset[0], coords[1] + offset[1]]
        ).filter(adjacent =>
            0 <= adjacent[0] && adjacent[0] <= width - 1 &&
            0 <= adjacent[1] && adjacent[1] <= height - 1
        );
    };

    const cellContents = (cells: string[][], coords: [number, number]): string =>
        cells[coords[0]][coords[1]];

    const tick = (cells: string[][]): string[][] => {
        const result: string[][] = [];

        for (let y = 0; y < height; y++) {
            result.push([]);
            const row: string[] = cells[y];
            for (let x = 0; x < width; x++) {
                const numOfAdjacentOccupants =
                    adjacentCoords([x, y]).map(
                        coords => cellContents(cells, coords)
                    ).filter(
                        cell => cell == "#"
                    ).length;
                
                if (row[x] == "L" && numOfAdjacentOccupants == 0) {
                    result[y].push("#");
                } else if (row[x] == "#" && numOfAdjacentOccupants >= 4) {
                    result[y].push("L");
                } else {
                    result[y].push(row[x]);
                }
            }
        }

        return result;
    };

    const startingGrid: string[][] = input.map(row => row.split(""));
    let currentGrid = startingGrid;
    let newGrid: string[][];
    let currStr: string, newStr: string;

    do {
        newGrid = tick(currentGrid);
        currStr = currentGrid.map(row => row.join("")).join("\n");
        newStr = newGrid.map(row => row.join("")).join("\n");

        if (currStr == newStr) {
            break;
        } else {
            currentGrid = newGrid;
        }
    } while (true);

    console.log(`After everyone stops moving, the number of occupied seats is ${newStr.split("").filter(c => c == "#").length}`);    
});
