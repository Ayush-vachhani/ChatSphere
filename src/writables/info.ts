import { writable } from "svelte/store";
export const user = writable({
    name: '',
    email: '',
    initials: '',
    full_name: ''
});

export const urls = writable({
    base: 'http://localhost:8000',
});