import { readFile } from "fs";
readFile("13/input.txt", (err, data) => {
    if (err) throw err;

    const input = data.toString().split("\r\n");
    const target = parseInt(input[0]);
    const buses = input[1].split(",").map(n => parseInt(n));
    
    const waitingTimes = buses.map(id => {
        if (isNaN(id))
            return Infinity;

        return target % id;
    });

    const earliestTime = Math.min(...waitingTimes);
    const earliestBusID = buses[waitingTimes.indexOf(earliestTime)];

    console.log(`The earliest bus is the number ${earliestBusID} and you'll be waiting ${earliestTime} units of time for it.`);
    console.log(`The product of these two numbers is ${earliestTime * earliestBusID}`);    

});
