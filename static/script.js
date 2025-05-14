const apiUrl = "http://127.0.0.1:8000/todos";

async function fetchTodos() {
    const res = await fetch(apiUrl);
    const todos = await res.json();

    const list = document.getElementById("todo-list");
    list.innerHTML = "";
    todos.forEach(todo => {
        const li = document.createElement("li");
        li.textContent = `${todo.name}: ${todo.desc}`;
        const del = document.createElement("button");
        del.textContent = "❌";
        del.onclick = () => deleteTodo(todo.id);
        li.appendChild(del);
        list.appendChild(li);
    });
}

async function handleSubmit(event) {
    event.preventDefault(); // prevent form from reloading the page

    const name = document.getElementById("name").value.trim();
    const desc = document.getElementById("desc").value.trim();

    if (!name || !desc) return;

    await fetch(apiUrl, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ name, desc })
    });

    document.getElementById("name").value = "";
    document.getElementById("desc").value = "";
    fetchTodos();
}

async function deleteTodo(id) {
    await fetch(`${apiUrl}/${id}`, {
        method: "DELETE"
    });
    fetchTodos();
}

fetchTodos();
