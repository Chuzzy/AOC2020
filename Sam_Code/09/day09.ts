import { readFile } from "fs";
readFile("09/input.txt", (err, data) => {
    if (err) throw err;

    const input = data.toString().split("\r\n").map(n => parseInt(n));

    let target: number;

    const sum = (nums: number[]): number => nums.reduce((total, count) => total + count, 0);

    for (let i = 25; i < input.length; i++) {
        const element = input[i];
        const last25 = input.slice(i - 25, i);
        if (!last25.some((x, j) => last25.some((y, k) => j != k && x + y == element))) {
            console.log(`At index ${i}, ${element} is not the sum of any two of the 25 numbers that precede it.`);
            target = element;
            break;
        }
    }

    for (let i = 0; i < input.length; i++) {
        for (let j = i + 1; j < input.length; j++) {
            const partition = input.slice(i, j + 1);
            const sliceSum = sum(partition);
            if (sliceSum === target) {
                console.log(`The numbers from indicies ${i} - ${j} match the target.`);
                console.log("The set is " + partition);
                console.log(`The sum of the smallest and largest number is ${Math.min(...partition) + Math.max(...partition)}`);
                return;
            }
        }
    }
});
