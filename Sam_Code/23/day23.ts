import { readFile } from "fs";
readFile("23/input.txt", (err, data) => {
    if (err) throw err;
    let input = data.toString();
});
