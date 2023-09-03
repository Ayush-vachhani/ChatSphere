<script lang="ts">
    import { onMount } from "svelte";
    import axios from "axios";
    import type {AxiosResponse} from 'axios';
    import {urls} from '../../writables/info.ts';
    let postsArray: any[] = [];

    interface Post {
    id: number;
    caption: string;
    image: string;
    likes: number;
    comments: number;
    // Add other fields as necessary
}

    onMount(async () => {
        const response: AxiosResponse<any, any> = await axios.get(`${$urls.base}/api/posts`);
        let res = response.data.posts.map((post: Post) => {
            post.image = `http://localhost:8000${post.image}`;
            return post;  // Return the modified post object
        });
        postsArray = [...postsArray, ...res];
        console.log(postsArray);
    });
</script>


<div class="container mx-auto px-4 bg-gray-100 min-h-screen">
    <!-- Navbar -->
    <nav class="flex justify-between items-center py-4 bg-gradient-to-r from-blue-500 to-purple-500 text-white shadow-md">
        <div class="text-2xl font-bold ml-4">MySocial</div>
        <div class="flex items-center mr-4">
            <input
                type="text"
                placeholder="Search..."
                class="border rounded px-4 py-2 mr-4 shadow-md"
            />
            <span class="material-icons text-gray-400">search</span>
        </div>
    </nav>

    <!-- Main Content -->
    <div class="flex mt-6">
        <!-- Sidebar -->
        <aside class="w-1/4 pr-4">
            <ul>
                <li class="mb-4">
                    <a href="/" class="text-blue-500 hover:text-blue-700 font-semibold">Home</a>
                </li>
                <li class="mb-4">
                    <a href="/users" class="hover:text-gray-700 font-semibold">Chat with other users</a>
                </li>
                <li class="mb-4">
                    <a href="www.google.com" class="hover:text-gray-700 font-semibold">Profile</a>
                </li>
            </ul>
        </aside>

        <!-- Posts -->
        <main class="w-2/4 bg-white p-4 rounded shadow-md">
            {#each postsArray as post}
                <div class="mb-6 border rounded p-4 hover:shadow-lg transition-shadow duration-300">
                    <img
                        src={post.image}
                        alt="Post content"
                        class="w-full h-64 object-cover rounded mb-2"
                    />
                    <p class="mt-2 text-gray-700">{post.caption}</p>
                    <div class="flex justify-between mt-2 text-gray-600">
                        <div>
                            <span class="material-icons text-red-500">favorite</span>
                            {post.likes} Likes
                        </div>
                        <div>
                            <span class="material-icons text-blue-500">COMMENTS</span>
                            {#each post.comments as comment}
                                <div class="flex justify-between mt-2 text-gray-600">
                                    <div>
                                        {comment.sender}: {comment.message}
                                    </div>
                                </div>
                            {/each}
                        </div>
                    </div>
                </div>
            {/each}
        </main>

        <!-- Right Sidebar (for ads, trending tags, etc.) -->
        <aside class="w-1/4 pl-4">
            <!-- ... -->
        </aside>
    </div>
</div>
