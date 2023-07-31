export const getData = async (url:string, params: Record<string, any>):Promise<any> => { //gets data from the API
    const searchParams:URLSearchParams = new URLSearchParams();
    Object.entries(params).forEach(([key, value]):void => {
        searchParams.append(key, String(value));
    });
    const response:globalThis.Response = await fetch(`${url}?${searchParams}`);
    return await response.json();
};