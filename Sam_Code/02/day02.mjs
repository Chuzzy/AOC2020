import { readFile } from "fs";
readFile("02/input.txt", (err, data) => {
    if (err) throw err;
    const re = /(?<min>\d+)-(?<max>\d+) (?<char>\w): (?<password>.+)/g;
    let oldPwPolicyValidCount = 0;
    let newPwPolicyValidCount = 0;
    
    for (const match of data.toString().matchAll(re)) {
        const min = parseInt(match.groups.min);
        const max = parseInt(match.groups.max);
        const count = [...match.groups.password.matchAll(match.groups.char)].length;
        const password = match.groups.password;
        const char = match.groups.char;

        // Old password policy
        if (min <= count && count <= max) oldPwPolicyValidCount++;

        // New password policy
        if (password[min - 1] == char ^ password[max - 1] == char) newPwPolicyValidCount++;
    }

    console.log(oldPwPolicyValidCount + " valid passwords according to the password policy rules from the shopkeeper's old job at the sled rental place down the street.");
    console.log(newPwPolicyValidCount + " valid passwords according to The Official Toboggan Corporate Policy.");
    
});
