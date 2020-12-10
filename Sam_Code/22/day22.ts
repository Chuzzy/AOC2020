import { readFile } from "fs";
readFile("22/input.txt", (err, data) => {
    if (err) throw err;

    const input = data.toString().split("\r\n");
});
