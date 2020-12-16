import { readFile } from "fs";

readFile("07/input.txt", (err, data) => {
    if (err) throw err;

    const input = data.toString().split("\r\n");
    const re = /^(?<bigbag>.+) bags contain (?<smallbags>(?:\d+ .+ bags?[,.]){1,}|no other bags\.)$/;
    const smallBagsRe = /(?<count>\d+) (?<color>\D+) bags?/g;

    const bags = [];

    for (const line of input) {
        const match = re.exec(line);
        const bigbag = match.groups.bigbag;
        if (match.groups.smallbags == "no other bags") {
            /*
            const newBag: Baggage = { bag: bigbag, contains: null };
            bags.push(newBag);
            */
        } else {
            for (const smallbag of match.groups.smallbags.matchAll(smallBagsRe)) {
                // const newBag: Baggage = { bag: bigbag, contains: smallbag.groups.color, count: parseInt(smallbag.groups.count) };
                bags.push([bigbag, smallbag.groups.color]);
            }
        }
    }

    const numberOfBagsWithShinyGold = -1 // bags.filter(bag => dfs(bags, bag[0]).includes("shiny gold"));
    console.log(`The number of bags that contain shiny gold bags are ${numberOfBagsWithShinyGold}`);

});
