<!-- SYNTAX TEST "Packages/User/vue-syntax-highlight/Vue Component.sublime-syntax" -->

<style lang="stylus">
font-stack = Helvetica, sans-serif
// ^ source.stylus
primary-color = #999
body
  font 100% font-stack
  color primary-color
</style>

<style lang="scss">
@import '~foo';
// ^ source.scss

a {
  color: red;
}
</style>

<style lang="sass">
@import '~foo'
// ^ source.sass
a
  color: red
</style>

<template lang="pug">
div.app
  h1.title This is the app
  // ^ source.pug
  comp-a(foo="bar", :a=1)
  comp-b(bar="baz", :a=234)
</template>

<script lang="coffee">
module.exports =
  data: ->
    msg: 'Hello from coffee!'
    # ^ source.coffee
</script>
