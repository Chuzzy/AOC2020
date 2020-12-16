import { readFile } from "fs";

const executeProgram = (program: string[], indexOfInstructionToInvert: number): [number, boolean] => {
    let executedInstructions: number[] = [];
    let accumulator = 0;
    for (let i = 0; i < program.length; i++) {
        if (executedInstructions.includes(i)) {
            console.log(`Instruction ${i} was about to be executed twice.`);
            console.log(`The accumulator's value is ${accumulator}`);
            return [accumulator, false];
        } else {
            executedInstructions.push(i);
            let [operation, argument] = program[i].split(" ");

            if (i == indexOfInstructionToInvert) {
                console.log(`[${i}] Flipping this instruction!`);
                operation = operation == "nop" ? "jmp" : operation == "jmp" ? "nop" : operation;
            }

            switch (operation) {
                case "nop":
                    console.log(`[${i}] No operation`);
                    break;
                case "acc":
                    accumulator += parseInt(argument);
                    console.log(`[${i}] Incremented accumulator by ${argument}; it's now at ${accumulator}`);
                    break;
                case "jmp":
                    const oldI = i;
                    i += parseInt(argument) - 1;
                    console.log(`[${oldI}] Jumped to ${i}`);                    
                    break;
                default:
                    throw new Error(`Excuse me, what is a ${operation}?`);
            }
        }
    }
    console.log(`The accumulator's value is ${accumulator}`);
    return [accumulator, true];
}


readFile("08/input.txt", (err, data) => {
    if (err) throw err;

    const input = data.toString().split("\r\n");

    for (let i = 0; i < input.length; i++) {
        const result = executeProgram(input, i);
        if (result[1]) {
            console.log(`The program terminated when instruction ${i} was flipped.`);
            break;
        }
    }
});
