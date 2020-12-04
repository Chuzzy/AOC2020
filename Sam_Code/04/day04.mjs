import { readFile } from "fs";
readFile("04/input.txt", (err, data) => {
    if (err) throw err;

    const input = data.toString().split("\r\n\r\n").map(s => s.replace(/\r\n/g, " "));
    let validPassportCount = 0;
    let validDataCount = 0;

    for (const passport of input) {
        if (["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"].every(field => passport.includes(field))) {
            validPassportCount++;

            const birthYear = parseInt(passport.match(/byr:(\d+)/)[1]);
            if (1920 <= birthYear && birthYear <= 2002) {
                const issueYear = parseInt(passport.match(/iyr:(\d+)/)[1]);
                if (2010 <= issueYear && issueYear <= 2020) {
                    const expYear = parseInt(passport.match(/eyr:(\d+)/)[1]);
                    if (2020 <= expYear && expYear <= 2030) {
                        const heightMatch = passport.match(/hgt:(\d+)(cm|in)/);
                        if (heightMatch) {
                            const height = parseInt(heightMatch[1])
                            if ((heightMatch[2] == "cm" && 150 <= height && height <= 193) || (59 <= height && height <= 76)) {
                                if (passport.match(/hcl:#[\da-f]{6}/)) { // Hair color
                                    if (passport.match(/ecl:(?:amb|blu|brn|gry|grn|hzl|oth)/)) { // Eye color
                                        const passportIdMatch = passport.match(/pid:(\d+)/);
                                        if (passportIdMatch) {
                                            if (passportIdMatch[1].match(/^[\d]{9}$/)) {
                                                validDataCount++;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

        }
    }

    console.log(`There are ${validPassportCount} valid passports.`);
    console.log(`Of these, there are ${validDataCount} passports with valid data.`);
});
