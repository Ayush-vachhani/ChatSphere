<script lang="ts">
	import axios from "axios";
	import { onMount } from "svelte";
	import { user } from "../../writables/info.ts";
	import Loading from "../../lib/Loading.svelte";
	let isLoading = true;

	let users: string[] = [];

	onMount(async () => {
		const response = await axios.get("http://127.0.0.1:8000/api/users");
		users = response.data.UserNames;
		console.log($user.full_name);
		users = users.filter((item) => item != $user.full_name);
		console.log(users);
		isLoading = false;
	});
</script>

<main>
	{#if isLoading}
		<Loading />
	{:else}
		{#each users as user}
			{#if user}
				<a href="/users/chat-with-{user.replace(/\s+/g, '_')}">{user}</a
				>
			{/if}
		{/each}
	{/if}
</main>

<style>
	main {
		background-color: #f5f5f5;
		padding: 20px;
	}

	a {
		display: block;
		color: #333;
		text-decoration: none;
		margin-bottom: 10px;
		padding: 10px;
		border-radius: 5px;
		background-color: #fff;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
	}

	a:hover {
		background-color: #f5f5f5;
	}
</style>
