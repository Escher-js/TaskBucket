import React, { useState } from 'react';

const CreateTask = ({ onSubmit }) => {
    const [name, setName] = useState('');
    const [detail, setDetail] = useState('');
    const [urgency, setUrgency] = useState(1);
    const [importance, setImportance] = useState(1);

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit({ name, detail, urgency, importance });
        setName('');
        setDetail('');
        setUrgency(1);
        setImportance(1);
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Name:
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
            </label>
            <label>
                Detail:
                <textarea value={detail} onChange={(e) => setDetail(e.target.value)} />
            </label>
            <label>
                Urgency:
                <input type="number" min="1" max="5" value={urgency} onChange={(e) => setUrgency(e.target.value)} />
            </label>
            <label>
                Importance:
                <input type="number" min="1" max="5" value={importance} onChange={(e) => setImportance(e.target.value)} />
            </label>
            <button type="submit">Create Task</button>
        </form>
    );
};

export default CreateTask;
