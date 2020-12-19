import { readFile } from "fs";

class Node {
    public children: Node[] = [];
    constructor(public value: number) {
    }

    public addChild(num: number) {
        const difference: number = num - this.value;
        if (1 <= difference && difference <= 3) {
            const newNode = new Node(num);
            this.children.push(newNode);
        }
    }
}


readFile("10/input.txt", (err, data) => {
    if (err) throw err;

    const input = data.toString().split("\r\n").map(n => parseInt(n)).sort((a, b) => a - b);
    const adapters = [0, ...input, Math.max(...input) + 3];

    const oneJoltIncreaseCount = adapters.filter((joltage, i, joltages) => i < joltages.length - 1 && joltage + 1 == joltages[i + 1]).length;
    const threeJoltIncreaseCount = adapters.filter((joltage, i, joltages) => i < joltages.length - 1 && joltage + 3 == joltages[i + 1]).length;

    console.log(`There are ${oneJoltIncreaseCount} one jolt increases and ${threeJoltIncreaseCount} three jolt increases.`);
    console.log(`The product of these numbers is ${oneJoltIncreaseCount * threeJoltIncreaseCount}`);

    let numberOfDistinctArrangements = 0;
    
    const tree = new Node(0);
    console.log(`The number of distinct arrangements is ${numberOfDistinctArrangements}.`);
    
});
