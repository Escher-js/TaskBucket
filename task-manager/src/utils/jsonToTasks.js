export const jsonToTasks = (jsonData) => {
    const tasks = new Array(5).fill(null).map(() => new Array(5).fill(null).map(() => []));

    jsonData.forEach((item) => {
        const i = 5 - item.importance;
        const j = item.urgency - 1;
        tasks[i][j].push(item.name);
    });

    return tasks;
};
