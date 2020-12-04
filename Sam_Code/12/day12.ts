import { readFile } from "fs";
readFile("12/input.txt", (err, data) => {
    if (err) throw err;
    let input = data.toString();
});
