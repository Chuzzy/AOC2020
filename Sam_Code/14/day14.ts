import { readFile } from "fs";
readFile("14/input.txt", (err, data) => {
    if (err) throw err;

    const input = data.toString().split("\r\n");
});
