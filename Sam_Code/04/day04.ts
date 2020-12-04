import { readFile } from "fs";
readFile("04/input.txt", (err, data) => {
    if (err) throw err;

    const input = data.toString().split("\r\n\r\n").map(s => s.replace(/\r\n/g, " "));
    const hasRequiredFields = (passportStr) => {
        return ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"].every(field => passportStr.includes(field));
    }

    const passportToObj = (passportStr) => {
        const obj = {};
        for (const pair of passportStr.matchAll(/(?<field>\w+):(?<val>\S+)/g)) {
            obj[pair.groups.field] = pair.groups.val;
        }
        return obj;
    }

    const numInRange = (x, min, max) => {
        x = x.toString();
        if (x.match(/^(\d+)$/)) {
            const num = parseInt(x);
            return min <= num && num <= max;
        }
        return false;
    }

    const isValidHeight = (heightStr) => {
        if (heightStr.match(/^(\d+)(cm|in)$/)) {
            return heightStr.endsWith("cm") ?
                numInRange(parseInt(heightStr), 150, 193) :
                numInRange(parseInt(heightStr), 59, 76);
        }
        return false;
    }

    const hasValidFields = (passportObj) => {
        return numInRange(passportObj.byr, 1920, 2020) &&
            numInRange(passportObj.iyr, 2010, 2020) &&
            numInRange(passportObj.eyr, 2020, 2030) &&
            isValidHeight(passportObj.hgt) &&
            passportObj.hcl.match(/^#[\da-f]{6}$/) &&
            passportObj.ecl.match(/^(?:amb|blu|brn|gry|grn|hzl|oth)$/) &&
            passportObj.pid.match(/^[\d]{9}$/);
    }

    console.log(`There are ${input.filter(hasRequiredFields).length} valid passports.`);
    console.log(`Of these, there are ${input.filter(hasRequiredFields).map(passportToObj).filter(hasValidFields).length} passports with valid data.`);
});
