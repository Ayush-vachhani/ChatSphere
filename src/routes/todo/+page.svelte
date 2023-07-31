<script>
    import axios from 'axios';
    import { onMount } from "svelte";
    let todos = [];
    onMount(fetchTodos);
    async function fetchTodos() {
        try {
            const response = await axios.get("http://localhost:8000/api/todo");
            todos = response.data;
        } catch (error) {
            console.error("Error fetching todos:", error);
        }
    }
    // creating new To-do
    async function createTodo(event) {
    try {
        const name = event.target.elements.name.value;
        todos['message'] = [...todos.message, name];
        event.target.reset();
        await axios.post('http://localhost:8000/api/todo', { name });
    } catch (error) {
        console.error('Error creating todo:', error);
    }
  }
  async function deleteMessage(id) {
    try {
        todos['message'] = todos['message'].filter((item) => item !== id);
        await axios.delete(`http://localhost:8000/api/todo`, { data: { val: id } });
    } catch (error) {
      console.error('Error deleting message:', error);
    }
  }
</script>

<main>
    <form on:submit|preventDefault={createTodo}>
        <input type="text" name="name" placeholder="Enter todo name" autocomplete="new-password" />
        <button>Create Todo</button>
    </form>
    {#if todos.length === 0}
        <p>Nothing to show!</p>
    {:else}
        <ul>
            {#each todos.message as todo}
                <li>{todo}</li>
                <button on:click={() => deleteMessage(todo)}>Delete</button>
            {/each}
        </ul>
    {/if}
</main>

<style>
    button {
        background-color: #4CAF50;
        border: 2px solid red;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
    }
</style>