<script setup>
import { ref } from "vue"
import { SERVER_URL } from "../config";
import { useRouter } from "vue-router";

const reviewId = ref(null)
const review = ref("")
const router = useRouter()

function submit() {
    fetch(`${SERVER_URL}/api/edit`, {
        method: 'POST',
        // credentials: 'include',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: reviewId.value, ctx: review.value })
    })
    .then((resp) => {
        if (!String(resp.status).match(/20[\d]/)) {
            alert("403 permission denied")
        } else {
            alert("您的回饋已編輯成功囉！")
            router.push('/view')
        }
    })
    .catch(() => {
        alert("我們遭遇技術上的問題，找助教")
    })
}
</script>

<template>
    <div class="h-full w-full">
        <div class="text-xl font-bold">修改</div>
        <div class="form-control">
            <label class="label">
                <span class="label-text">修改回饋之 ID</span>
            </label>
            <div
                class="inline-block animate-border rounded-xl bg-white from-teal-500 via-purple-500 to-pink-500 bg-[length:400%_400%] p-0.5 transition bg-gradient-to-r shadow-lg focus:outline-none focus:ring"
            >
                <input type="text" v-model="reviewId" class="block rounded-xl textarea textarea-bordered focus:ring-0 focus:ring-offset-0 w-full">
            </div>
        </div>
        <div class="mt-2" />
        <div class="form-control">
            <label class="label">
                <span class="label-text">修改回饋之內容</span>
            </label>
            <div
                class="inline-block animate-border rounded-xl bg-white from-teal-500 via-purple-500 to-pink-500 bg-[length:400%_400%] p-0.5 transition bg-gradient-to-r shadow-lg focus:outline-none focus:ring"
            >
                <textarea v-model="review" class="block rounded-xl textarea textarea-bordered focus:ring-0 focus:ring-offset-0 h-48 w-full"></textarea>
            </div>
        </div>
        <div class="mt-2" />
        <div
            class="inline-block animate-border rounded-xl bg-white from-teal-500 via-purple-500 to-pink-500 bg-[length:400%_400%] p-0.5 transition bg-gradient-to-r shadow-lg focus:outline-none focus:ring"
        >
            <button class="btn btn-wide btn-ghost text-white" @click="submit">Submit</button>
        </div>
        <p class="mt-4">
            親愛的同學：<br />
            本學期已進入後半段，您現在一定很忙碌於學業吧，加油！加油！<br />
            課程意見調查均採匿名方式填答，無論教師端或行政端皆不會顯示同學系所、姓名及學號等身份資料。<br />
            請同學們以<span class="text-accent font-bold">中肯、公平、公正與負責</span>的態度填答及提出建言，切勿使用侮辱、謾罵或人身攻擊等文字，因而觸法。
            <br /><br />
            祝同學們<br /><br />
            身體健康  學業進步<br />
        </p>
    </div>
</template>
