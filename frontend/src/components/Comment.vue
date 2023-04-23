<template>
  <div
    class="
      rounded-lg
      border-2
      border-gray-300
      m-5
      bg-gray-100
    "
  >
    <ul
      class="
        flex
        flex-row
        justify-between
        m-4
      "
    >
      <li
        class="
          text-lg
        "
      >
        {{this.comment.userName}}
      </li>

      <li>
        {{this.comment.date}}
      </li>
    </ul>
    <div
      class="
        m-4
      "
    >
      {{this.comment.text}}
    </div>
  </div>
</template>

<script>
export default {
  name: "Comment",
  props: {
    comment: Object,
  },
}
</script>
