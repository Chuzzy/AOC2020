import { readFile } from "fs";
readFile("11/input.txt", (err, data) => {
    if (err) throw err;
    let input = data.toString();
});
