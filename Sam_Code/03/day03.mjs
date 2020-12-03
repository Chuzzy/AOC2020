import { readFile } from "fs";
readFile("03/input.txt", (err, data) => {
    if (err) throw err;

    const input = data.toString().split("\n");
    function simulateSlope(xStep, yStep) {
        const inputWidth = input[0].length;
        let treesEncountered = 0;
        let x = 0;
        for (let y = 0; y < input.length; y += yStep) {
            if (input[y][x] == "#") treesEncountered++;
            x = (x + xStep) % inputWidth;
        }
        return treesEncountered;
    }
    console.log(simulateSlope(3, 1) + " trees encountered on the way down when going right 3 down 1.");

    const slopes = [simulateSlope(1, 1,), simulateSlope(3, 1), simulateSlope(5, 1), simulateSlope(7, 1), simulateSlope(1, 2)];
    console.log("The different number of trees encountered are " + slopes);
    console.log("The product is " + slopes.reduce((total, n) => total * n, 1));
});
