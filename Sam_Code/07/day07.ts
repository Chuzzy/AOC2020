import { readFile } from "fs";
import { stringify } from "querystring";

readFile("07/input.txt", (err, data) => {
    if (err) throw err;

    const input = data.toString().split("\r\n");
    const re = /^(?<bigbag>.+) bags contain (?<smallbags>(?:\d+ .+ bags?[,.]){1,}|no other bags\.)$/;
    const smallBagsRe = /(?<count>\d+) (?<color>\D+) bags?/g;

    interface DirectedEdge {
        from: string;
        to: string;
    }

    const tree: DirectedEdge[] = [];
    const sameEdge = (e1: DirectedEdge, e2: DirectedEdge): boolean => e1.from === e2.from && e1.to === e2.to;

    for (const line of input) {
        const match = re.exec(line);
        const bigbag = match.groups.bigbag;
        for (const smallbag of match.groups.smallbags.matchAll(smallBagsRe)) {
            const newEdge: DirectedEdge = {from: bigbag, to: smallbag.groups.color};
            if (tree.findIndex(edge => sameEdge(edge, newEdge)) === -1) {
                tree.push(newEdge);
            }
        }
    }


    const dfs = (node: DirectedEdge) => {
        if (node.to === "shiny gold") {
            return true;
        }
        return dfs(tree[tree.findIndex(edge => edge.from === node.to)]);
    }

    console.log(dfs(tree[0]));
    
});
