import { readFile } from "fs";
readFile("05/input.txt", (err, data) => {
    if (err) throw err;
    console.log(9 + 10);
    console.log(data.toString());
});
