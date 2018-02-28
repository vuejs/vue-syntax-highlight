<!--
Things to verify:
- comments (this block) are properly highlighted
- expressions are highlighted as JS
- <script> highlights ES2015 syntax
- <style> highlights as CSS
-->

<template>
  <div>
    {{ foo * 10 + 'hi' }}
    <span
      v-text="foo * 10 + 'hi'"
      :id="foo + 'baz'"
      @click="onClick('hello')"
      @click.prevent="onClick('hello')">
      Hello
    </span>
  </div>
</template>

<script>
export default {
  data: () => ({
    foo: 'bar'
  })
}
</script>

<style>
div {
  color: red;
}
</style>
