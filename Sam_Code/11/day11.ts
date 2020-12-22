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
        cells[coords[1]][coords[0]];

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

    const raycastSeat = (cells: string[][], coords: [number, number], direction: [number, number]): string => {
        const newPos: [number, number] = [coords[0] + direction[0], coords[1] + direction[1]];

        if (0 > newPos[0] || newPos[0] > width - 1 || 0 > newPos[1] || newPos[1] > height - 1) {
            return ".";
        }

        const contents = cellContents(cells, newPos);

        if (contents == ".") {
            return raycastSeat(cells, newPos, direction);
        } else {
            return contents;
        }
    };

    const tick2 = (cells: string[][]): string[][] => {
        const result: string[][] = [];
        const cardinalDirections: [number, number][] = [
            [-1, -1],
            [0, -1],
            [1, -1],
            [1, 0],
            [1, 1],
            [0, 1],
            [-1, 1],
            [-1, 0]
        ];

        for (let y = 0; y < height; y++) {
            result.push([]);
            const row: string[] = cells[y];
            for (let x = 0; x < width; x++) {
                const numOfVisibleOccupants: number =
                    cardinalDirections.map(
                        direction => raycastSeat(cells, [x, y], direction)
                    ).filter(
                        cell => cell == "#"
                    ).length;

                if (row[x] == "L" && numOfVisibleOccupants == 0) {
                    result[y].push("#");
                } else if (row[x] == "#" && numOfVisibleOccupants >= 5) {
                    result[y].push("L");
                } else {
                    result[y].push(row[x]);
                }
            }
        }

        return result;
    };

    currentGrid = startingGrid;
    newGrid = [];
    currStr = ""; newStr = "";

    do {
        newGrid = tick2(currentGrid);
        currStr = currentGrid.map(row => row.join("")).join("\n");
        newStr = newGrid.map(row => row.join("")).join("\n");

        if (currStr == newStr) {
            break;
        } else {
            currentGrid = newGrid;
        }
    } while (true);

    console.log(`After everyone stops moving AGAIN, the number of occupied seats is ${newStr.split("").filter(c => c == "#").length}`);
});
