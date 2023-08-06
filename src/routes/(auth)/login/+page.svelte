<script lang="ts">
    import axios from "axios";
    import type {AxiosResponse} from 'axios';
    import { goto } from "$app/navigation";
    import { user } from "../../../writables/info.ts";
    async function handlePost(event) {
        const formData: FormData = new FormData(event.target);
        const data: any = {};
        formData.forEach((value: FormDataEntryValue, key: string): void => {
                data[key] = value;
            }
        );
        try {
            const response: AxiosResponse<any, any> = await axios.post('http://127.0.0.1:8000/api/login', data, {});
            const name = response.data.user.name;
            const email = response.data.user.email;
            const initials = response.data.user.initials;
            const full_name = response.data.user.full_name;
            user.set({name, email, initials, full_name});
            localStorage.setItem('token', JSON.stringify(response.data.user));
            await goto('/');
        } catch (error) {
            console.clear();
            alert("Invalid credentials, please try again");
            event.target.reset();
        }
    }
</script>

<body>
<form action="http://127.0.0.1:8000/api/login" method="POST" on:submit|preventDefault={handlePost}>
    <label>Email:<input autocomplete="email" name="email" required type="email" /></label>
    <label>Password:<input autocomplete="current-password" name="password" required type="password" /></label>
    <button type="submit">LOGIN</button>
</form>
</body>

<style>
    body {
        justify-content: center;
        align-items: center;
        background-image: url(https://www.wallpaperflare.com/static/561/8/12/abstract-waveforms-green-digital-wallpaper.jpg);
        background-position: center center;
        min-height: 100vh;
    }
    
    form {
        display: flex;
        flex-direction: column;
        gap: 1rem;
        max-width: 400px;
        margin: 0 auto;
    }
    
    label {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }
    
    input {
        padding: 0.5rem;
        border-radius: 0.25rem;
        border: 1px solid #ccc;
    }
    
    button {
        padding: 0.5rem;
        border-radius: 0.25rem;
        border: none;
        background-color: #333;
        color: #fff;
        cursor: pointer;
    }
</style>
