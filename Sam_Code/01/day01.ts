import { readFile } from "fs";
readFile("01/input.txt", (err, data) => {
    if (err) throw err;
    let input = data.toString().split("\n").map(n => parseInt(n));

    console.log("First half: ");
    first: {
        for (const a of input) {
            for (const b of input) {
                if (a + b == 2020) {
                    console.log("The answer is " + a + " and " + b);
                    console.log("The product of these is " + (a * b));
                    break first;
                }
            }
        }
    }

    console.log("Second half: ");
    second: {
        for (const a of input) {
            for (const b of input) {
                for (const c of input) {
                    if (a + b + c == 2020) {
                        console.log("The answer is " + a + " and " + b + " and " + c);
                        console.log("The product of these is " + (a * b * c));
                        break second;
                    }
                }
            }
        }
    }
});
