<script lang="ts">
	import axios from "axios";
	import { onMount } from "svelte";
	import { user } from "../../../writables/info.ts";
	let chatPartner = "";
	let messages: any[] = [];
	let socket: WebSocket;

	onMount(async () => {
		const path = window.location.pathname;
		const parts = path.split("/");
		chatPartner = parts[parts.length - 1].replace("chat-with-", "").replace(/_/g, " ");
		console.log(chatPartner);
		const user1_name = $user.full_name;
		const user2_name = chatPartner;
		const data = { user1_name, user2_name };
		const Response = await axios.post("http://127.0.0.1:8000/api/messages",data);
		messages = Response.data.messages;
		console.log(messages);
		//websockets
		socket = new WebSocket(`ws://127.0.0.1:8000/ws/chat`);
        socket.addEventListener("open", () => 
        {
            const message = {
                type: "join",
                room_name: [user1_name, user2_name]
            };
            socket.send(JSON.stringify(message));
            console.log("Connection is successful!");
        });
	});
</script>

<div class="min-h-screen bg-gray-100 flex flex-col">
	<div class="bg-gray-800 text-white py-4 text-center">
		<h1 class="text-2xl font-bold">Chat App</h1>
	</div>
	<div class="flex-1 p-4">
		{#each messages as message}
			<div class="flex p-1">
				<span class="font-bold mr-2">{message.sender}:</span>
				<div class="-chat-bubble mr-2 flex-grow">{message.message}</div>
				{#if $user.full_name === message.sender}
					<button class="-btn -btn-accent">Delete</button>
				{/if}
			</div>
		{/each}
	</div>
	<form class="bg-gray-200 p-4">
		<div class="flex">
			<input
				type="text"
				name="message"
				placeholder="Type your message"
				class="flex-1 p-2 rounded mr-2"
				autocomplete="off"
			/>
			<button type="submit" class="-btn -btn-primary">SEND</button>
		</div>
	</form>
</div>
