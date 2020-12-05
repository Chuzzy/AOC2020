import { readFile } from "fs";
readFile("21/input.txt", (err, data) => {
    if (err) throw err;

    const input = data.toString().split("\r\n");
});
