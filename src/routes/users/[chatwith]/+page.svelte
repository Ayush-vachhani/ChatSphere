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
		const user1_name = $user.full_name;
		const user2_name = chatPartner;
		const data = { user1_name, user2_name };
		const Response = await axios.post("http://127.0.0.1:8000/api/messages",data);
		messages = Response.data.messages;
		//websockets

		socket = new WebSocket(`ws://127.0.0.1:8000/ws/chat`);
		socket.addEventListener("open", () => {
			const message = {type: "join",room_name: [user1_name, user2_name],};
			socket.send(JSON.stringify(message));
			console.log("Connection is successful!");
		});
		socket.onmessage = (e) => {
			const message = JSON.parse(e.data);
			switch (message.type) {
				case "chat_message":
					messages = [...messages, message.context];
					break;
				case "delete":
					messages = messages.filter((item) =>item.message!=message.context.message || item.sender!=message.context.sender);
					break;
				default:
					break;
			}
		};
	});
	//sending messages
	async function sendMessage(event: Event) {
		event.preventDefault();
		if (event && event.target instanceof HTMLFormElement) {
			const sender = $user.full_name;
			const message = event.target.message.value;
			const type = "chat_message";
			const data = { sender, message, type };

			socket.send(JSON.stringify(data));
			event.target.reset();
		}
		if (event && event.target instanceof HTMLFormElement) {
			event.target.reset();
		}
	}
	async function deleteMessage(id: string) {
		try {
			const sender = $user.full_name;
			const message = id;
			const type = "delete";
			const data = { sender, message, type };
			socket.send(JSON.stringify(data));
		} catch (error) {
			console.error("Error deleting message:", error);
		}
	}
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
					<button
						class="-btn -btn-accent"
						on:click={() => deleteMessage(message.message)}
						>Delete</button
					>
				{/if}
			</div>
		{/each}
	</div>
	<form class="bg-gray-200 p-4" on:submit={sendMessage}>
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
