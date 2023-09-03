<script lang="ts">
    //skeleton ui
    import { Toast, toastStore } from '@skeletonlabs/skeleton';
    //lifecycle
    import { onMount} from 'svelte';
    import { goto } from "$app/navigation";
    //components
    import Navbar from '$lib/Navbar.svelte';
    import Loading from "$lib/Loading.svelte";
    //writable & stores
    import  {user} from '../writables/info.ts';
    //function
    import {email} from '../ts/email.ts';
    //stores
    let isloading = true,isLoggedIn=false;
    let t= {
        message: `WELCOME ${$user.name.toUpperCase()}`,
        timeout:2000,
    };
    onMount(() => {
        let temp = localStorage.getItem('token');
        let userObj
        if(temp!=null)
        {
            userObj = JSON.parse(temp)
            console.log(userObj);
        }
        if ($user.name=='')
        {
            if(temp!=null)
            {
                user.set({name:userObj.name, email:userObj.email, initials:userObj.initials,full_name:userObj.full_name});
            }
            else
            {
                console.log('NO user found');
            }
        }
        if ($user.name) {
            isLoggedIn = true;
            toastStore.trigger(t);
        }
        isloading = false;
    });
</script>

<main>
    {#if isloading}
        <Loading />
    {:else}
        <Toast max?=1 duration?=250 />
        <Navbar {isLoggedIn} />
        <a href="/users" class="-btn -btn-accent">Users</a>
    {/if}
</main>

<style lang="scss">

</style>
