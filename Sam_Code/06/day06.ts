import { readFile } from "fs";
readFile("06/input.txt", (err, data) => {
    if (err) throw err;

    const input = data.toString().split("\r\n\r\n");
    const groupsOfPeople: string[][] = input.map(group => group.split("\r\n"));
    const questionsAnswered: number[] = groupsOfPeople.map(person => new Set(person.join("")).size);
    console.log(`The number of unique answered questions per group in total is ${questionsAnswered.reduce((total, count) => total + count, 0)}`);

    const answeredByEveryoneElse = (question: string, otherAnswers: string[]): boolean => 
        otherAnswers.every(otherAnswer => otherAnswer.includes(question));

    const allQuestionsAnswered: number[] = groupsOfPeople.map(
        group => (group[0].split("").filter(q => answeredByEveryoneElse(q, group))).length
    );

    console.log(`The number of unique answered questions answered by everyone in each group in total is ${allQuestionsAnswered.reduce((total, count) => total + count, 0)}`);
});
