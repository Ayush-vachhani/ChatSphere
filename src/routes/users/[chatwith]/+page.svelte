<script>
  import { onMount } from 'svelte';

  let chatPartner = '';

  onMount(() => {
    const path = window.location.pathname;
    const parts = path.split('/');
    chatPartner = parts[parts.length - 1].replace('chat-with-', '').replace(/_/g, ' ');
    console.log(chatPartner);
    
  });
</script>

<main>
  <div class="chat-window">
    <div class="chat-header">
      Your chat with {chatPartner}
    </div>
    <div class="chat-messages">
      <!-- TODO: Display chat messages here -->
    </div>
    <div class="chat-input">
      <input type="text" placeholder="Type your message here..." />
      <button>Send</button>
    </div>
  </div>
</main>

<style>
  .chat-window {
    display: flex;
    flex-direction: column;
    height: 100%;
    padding: 16px;
  }

  .chat-header {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 16px;
  }

  .chat-messages {
    flex-grow: 1;
    overflow-y: auto;
    margin-bottom: 16px;
  }

  .chat-input {
    display: flex;
    align-items: center;
  }

  .chat-input input {
    flex-grow: 1;
    margin-right: 16px;
    padding: 8px;
    font-size: 16px;
  }

  .chat-input button {
    padding: 8px 16px;
    font-size: 16px;
    font-weight: bold;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
</style>