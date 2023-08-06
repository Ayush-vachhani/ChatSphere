<script lang="ts">
    import { onMount, onDestroy } from "svelte";
    import axios from "axios";
    import { user } from "../../writables/info.ts";

    //skeleton library
    import { Avatar } from '@skeletonlabs/skeleton';
    let messages: any[] = [];
    let socket: WebSocket;
    onMount(() => {
        socket = new WebSocket(`ws://127.0.0.1:8000/ws/chat`);
        socket.addEventListener("open", () => 
        {
            const message = {
                type: "join",
                room_name: 'room1'
            };
            socket.send(JSON.stringify(message));
            console.log("Connection is successful!");
        });
        socket.onmessage = (e) => 
        {
            const message = JSON.parse(e.data);
            switch (message.type) 
            {
                case "chat_message":
                    messages = [...messages, message.message];
                    break;
                case "delete":
                    console.log(message.message.message);
                    messages = messages.filter((item) => (item.message != message.message.message || item.name !== message.message.name));
                    break;
                default:
                    break;
            }
        };
    });

    async function getMessages() {
        const response = await axios.get("http://127.0.0.1:8000/api/users");
        messages = response.data.messages[0];
        console.log($user.name);
    }

    async function sendMessage(event: Event) {
        event.preventDefault();
        if (event && event.target instanceof HTMLFormElement) {
            const name = $user.name;
            const message = event.target.message.value;
            const type = "chat_message";
            const data = { name, message, type };

            socket.send(JSON.stringify(data));
            event.target.reset();
        }
        if (event && event.target instanceof HTMLFormElement) {
            event.target.reset();
        }
    }

    async function deleteMessage(id:string) {
    try {
        const name = $user.name;
        const message = id;
        const type = "delete";
        const data = { name, message, type };
        socket.send(JSON.stringify(data));
    } catch (error) {
      console.error('Error deleting message:', error);
    }
  }

    onMount(getMessages);
</script>

<div class="min-h-screen bg-gray-100 flex flex-col">
    <div class="bg-gray-800 text-white py-4 text-center">
        <h1 class="text-2xl font-bold">Chat App</h1>
    </div>
    <div class="flex-1 p-4">
        {#each messages as message}
            <div class="flex p-1">
                <Avatar initials={message.name[0]} background="bg-primary-400" />
                <span class="font-bold mr-2">{message.name}:</span>
                <div class="-chat-bubble mr-2 flex-grow">{message.message}</div>
                {#if $user.name === message.name}
                    <button class="-btn -btn-accent" on:click={() => deleteMessage(message.message)}>Delete</button>
                {/if}
            </div>
        {/each}
    </div>
    <form class="bg-gray-200 p-4" on:submit={sendMessage}>
        <div class="flex">
            <input type="text" name="message" placeholder="Type your message" class="flex-1 p-2 rounded mr-2" autocomplete="off"/>
            <button type="submit" class="-btn -btn-primary">SEND</button>
        </div>
    </form>
</div>