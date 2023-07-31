import axios from "axios";
import type {AxiosResponse} from 'axios';
export const email = async (toEmail: string): Promise<void> => {
    // const csrfToken:string|undefined = getCookie('csrftoken');
    // const headers = { 'X-CSRFToken': csrfToken };
    const data:{to_email:string} = { to_email: toEmail };
    try {
        const response:AxiosResponse<any,any> = await axios.post('http://localhost:8000/api/email', data, {});
        alert('Email has been sent');
    } catch (error) {
        alert('Could not send email');
    }
};

function getCookie(name: string): string | undefined {
    const value:string = `; ${document.cookie}`;
    const parts:string[] = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop()?.split(';').shift();
}

