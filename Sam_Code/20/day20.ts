import { readFile } from "fs";
readFile("20/input.txt", (err, data) => {
    if (err) throw err;

    const input = data.toString().split("\r\n");
});
