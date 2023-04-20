import React, { useState } from 'react';
import './TaskTable.css';

const TaskTable = ({ tasks }) => {
    const [draggedTask, setDraggedTask] = useState(null);

    const onDragStart = (e, task) => {
        e.dataTransfer.setData('text/plain', task);
        setDraggedTask(task);
    };

    const onDragOver = (e) => {
        e.preventDefault();
    };

    const onDrop = (e, i, j) => {
        e.preventDefault();
        const updatedTasks = [...tasks];
        const index = updatedTasks[i][j].indexOf(draggedTask);

        if (index !== -1) {
            updatedTasks[i][j].splice(index, 1);
        }

        updatedTasks[i][j].push(draggedTask);
        setDraggedTask(null);
    };

    const renderTasks = (i, j) => {
        return tasks[i][j].map((task) => (
            <span
                key={task}
                className="item"
                draggable="true"
                onDragStart={(e) => onDragStart(e, task)}
            >
                {task}
            </span>
        ));
    };

    return (
        <table className="task-table">
            <tbody>
                {tasks.map((row, i) => (
                    <tr key={i}>
                        {row.map((cell, j) => (
                            <td
                                key={j}
                                onDragOver={onDragOver}
                                onDrop={(e) => onDrop(e, i, j)}
                            >
                                {renderTasks(i, j)}
                            </td>
                        ))}
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default TaskTable;
