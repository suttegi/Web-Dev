const handleAddTask = () => {
    const taskContainer = document.querySelector(".task_container");
    const taskInput = document.querySelector("textarea");

    if (taskContainer && taskInput.value.trim() !== "") {
        if(taskInput.value.includes("_")) {
            alert("введите без спешл символов пж")
            
        }
        else{
            const newTask = document.createElement("li");
            newTask.classList.add("task-item");
    
            const checkbox = document.createElement("input");
            checkbox.type = "checkbox";
            checkbox.classList.add("isDone");
    
            const taskText = document.createElement("span");
            taskText.textContent = taskInput.value;
    
            const deleteButton = document.createElement("button");
            deleteButton.textContent = "del";
            deleteButton.classList.add("delete-task");
            deleteButton.onclick = () => newTask.remove();
    
            newTask.append(checkbox, taskText, deleteButton);
            taskContainer.appendChild(newTask);
            taskInput.value = "";

        }
    }
};

const handleTaskIsDone = () => {
    document.querySelectorAll(".isDone").forEach((checkbox) => {
        const taskItem = checkbox.parentElement;
        if (checkbox.checked) {
            taskItem.classList.add("done");
        } else {
            taskItem.classList.remove("done");
        }
    });
};

document.addEventListener("change", handleTaskIsDone);
