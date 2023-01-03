<script setup>
import { ref, computed, watchEffect } from "vue"
import { SERVER_URL } from "../config"
import { useRoute } from "vue-router";

const route = useRoute()
const ids = ref(null)
const viewContent = ref(null)
fetch(`${SERVER_URL}/api/view`)
    .then((resp) => resp.json())
    .then((resp) => {
        ids.value = resp
    })
    .catch(() => {
        alert("我們遭遇技術上的問題，找助教")
    })
const viewId = computed(() => {
    return route.params.id
})
watchEffect(() => {
    if (!viewId.value) return
    fetch(`${SERVER_URL}/api/view?id=${viewId.value}`)
        .then((resp) => resp.text())
        .then((resp) => {
            viewContent.value = resp
        })
        .catch(() => {
            alert("我們遭遇技術上的問題，找助教")
        })
})
</script>

<template>
    <div class="h-full w-full">
        <div class="flex w-full gap-x-4">
            <div>
                <div class="text-xl font-bold mb-4">查看</div>
                <ul class="menu bg-base-700 w-56">
                    <li v-for="_id in ids" :key="_id">
                        <router-link :to="`/view/${_id}`">{{ _id }}</router-link>
                    </li>
                </ul>
            </div>
            <div v-if="viewContent != null">
                <div class="text-xl font-bold mb-4">回饋</div>
                <div class="flex-1 w-full border-2 p-2">
                    <div v-html="viewContent"></div>
                </div>
            </div>
        </div>
    </div>
</template>
