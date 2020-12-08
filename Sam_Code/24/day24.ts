import { readFile } from "fs";
readFile("24/input.txt", (err, data) => {
    if (err) throw err;

    const input = data.toString().split("\r\n");
});
