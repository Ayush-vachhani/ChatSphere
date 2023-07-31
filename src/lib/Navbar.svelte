<script lang="ts">
	export let isLoggedIn:boolean;
	import { user } from '../writables/info.ts';
	function logout() {
        user.update(n => ({ ...n, name: '', email: '',initials: '' }));
		isLoggedIn = false;
        localStorage.clear();
	}
    //variables
    let logs = ['login','register'];
	//skeleton ui
    import { Avatar } from '@skeletonlabs/skeleton';
</script>
<main>
    {#if isLoggedIn}
        <nav>
            <h3>WELCOME, {$user.name.toUpperCase()}!</h3>
            <a href="/profile"><Avatar initials={$user.initials} background="bg-primary-600"/> PROFILE</a>
            <button on:click={logout} ><i class="fa-solid fa-right-from-bracket"></i> LOGOUT</button>
        </nav>
    {:else}
      <nav>
          <h3>WELCOME TO OUR SITE</h3>
          {#each logs as log}
              <a href="/{log}"><i class="fa-solid fa-user"></i> {log.toUpperCase()}</a>
          {/each}
      </nav>
    {/if}
</main>
<style lang="scss">
    nav{@apply flex justify-evenly items-center bg-purple-700 h-16;  }
    button{@apply text-white hover:bg-amber-400 h-16 w-1/6;}
    h3{@apply text-amber-400;}
    a{@apply flex items-center px-20 text-white hover:bg-amber-400 h-16 w-1/6 align-middle;}
</style>