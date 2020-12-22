import { readFile } from "fs";
readFile("12/input.txt", (err, data) => {
    if (err) throw err;

    const input = data.toString().split("\r\n");
    const parser = /(?<action>\w)(?<value>\d+)/;

    let x = 0, y = 0, bearing = 90;

    const turnLeft = (currBearing: number, degrees: number): number => {
        if (currBearing - degrees < 0)
            return turnLeft(currBearing + 360, degrees);

        return currBearing - degrees;
    };

    const turnRight = (currBearing: number, degrees: number): number => {
        if (currBearing + degrees > 360)
            return turnRight(currBearing - 360, degrees);

        return currBearing + degrees;
    };

    input.forEach(instruction => {
        const match = parser.exec(instruction);
        if (!match) throw new Error(`Excuse me, what does ${instruction} mean?`);

        const action = match.groups.action;
        const value = parseInt(match.groups.value);

        switch (action) {
            case "N":
                y += value;
                break;
            case "E":
                x += value;
                break;
            case "S":
                y -= value;
                break;
            case "W":
                x -= value;
                break;
            case "L":
                bearing = turnLeft(bearing, value);
                break;
            case "R":
                bearing = turnRight(bearing, value);
                break;
            case "F":
                switch (bearing) {
                    case 360:
                        bearing = 0;
                    case 0:
                        y += value;
                        break;
                    case 90:
                        x += value;
                        break;
                    case 180:
                        y -= value;
                        break;
                    case 270:
                        x -= value;
                        break;
                    default:
                        throw new Error(`Illegal bearing ${bearing}!`);
                }
                break;
            default:
                throw new Error(`I have no idea how to handle ${instruction}.`);
        }
    });

    console.log(`The ship is at (${x}, ${y}), bearing ${bearing}. The Manhattan distance is ${Math.abs(x) + Math.abs(y)}`);

    const ship = { x: 0, y: 0 };
    const waypt = { x: 10, y: 1 };

    const rotateLeft = (waypoint: { x: number, y: number }, degrees: number) => {
        const newX = -waypoint.y, newY = waypoint.x;

        if (degrees > 0) {
            waypoint.x = newX;
            waypoint.y = newY;
            rotateLeft(waypoint, degrees - 90);
        }
    };

    const rotateRight = (waypoint: { x: number, y: number }, degrees: number) => {
        const newX = waypoint.y, newY = -waypoint.x;

        if (degrees > 0) {
            waypoint.x = newX;
            waypoint.y = newY;
            rotateRight(waypoint, degrees - 90);
        }
    };

    input.forEach(instruction => {
        const match = parser.exec(instruction);
        if (!match) throw new Error(`Excuse me, what does ${instruction} mean?`);

        const action = match.groups.action;
        const value = parseInt(match.groups.value);

        switch (action) {
            case "N":
                waypt.y += value;
                break;
            case "E":
                waypt.x += value;
                break;
            case "S":
                waypt.y -= value;
                break;
            case "W":
                waypt.x -= value;
                break;
            case "L":
                rotateLeft(waypt, value);
                break;
            case "R":
                rotateRight(waypt, value);
                break;
            case "F":
                ship.x += waypt.x;
                ship.y += waypt.y;
                break;
            default:
                throw new Error(`I have no idea how to handle ${instruction}.`);
        }
    });


    console.log(`The waypoint is at (${waypt.x}, ${waypt.y}) and the ship is at (${ship.x}, ${ship.y}). The Manhattan distance is ${Math.abs(ship.x) + Math.abs(ship.y)}`);
});
