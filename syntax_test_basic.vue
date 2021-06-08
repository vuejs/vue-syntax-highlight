<!-- SYNTAX TEST "Packages/User/vue-syntax-highlight/Vue Component.sublime-syntax" -->

<template>
	<a @on.click="foo()">Click Me</a>
<!-- ^ text.html.vue -->
<!--              ^ source.js -->
    <span v-text="foo * 10 + 'hi'" :id="foo + 'baz'">Hello {{ world }}</span>
<!--              ^ source.js -->
<!--                          ^ meta.string.js -->
<!--                                     ^ source.js -->
<!--                                            ^ meta.string.js -->
<!--                                                           ^ source.js -->

</template>

<script>
	export default {
	// ^ source.js
	// ^ meta.export.js

		function () {

		}
	}
</script>

<style>
	body {
	/* ^ source.css */
		background-color: yellow;
	/*                     ^ meta.block.css */
	/*                     ^ meta.property.value.css */
	}
</style>
