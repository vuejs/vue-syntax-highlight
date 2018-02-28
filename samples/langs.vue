<!--
Things to verify:
- Langs are highlighted properly. Requires installing corresponding packages:
 - Stylus
 - Pug
 - Better CoffeeScript
-->

<style lang="stylus">
font-stack = Helvetica, sans-serif
primary-color = #999
body
  font 100% font-stack
  color primary-color
</style>

<style lang="scss">
@import '~foo';
a {
  color: red;
}
</style>

<style lang="sass">
@import '~foo'
a
  color: red
</style>

<template lang="pug">
div.app
  h1.title This is the app
  comp-a(foo="bar", :a=1)
  comp-b(bar="baz", :a=234)
</template>

<script lang="coffee">
module.exports =
  data: ->
    msg: 'Hello from coffee!'
</script>
