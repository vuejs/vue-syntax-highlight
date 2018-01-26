# Vue Syntax Highlight

**Note**: the `new` branch hosts the new syntax that only works in Sublime build > 3153. For the old syntax, see `master` branch.

Sublime Text Syntax highlighting for single-file [Vue.js](http://vuejs.org) components (enabled by [vue-loader](https://github.com/vuejs/vue-loader) or [vueify](https://github.com/vuejs/vueify)).

<p align="center">
  <img width="809px" src="https://raw.githubusercontent.com/vuejs/vue-syntax-highlight/new/samples/screenshot.png">
</p>

### Install

- Via Package Control: search for `Vue Syntax Highlight`.
- Manual: clone this repo into your Sublime `Packages` folder.

**NOTE:** You still need to install corresponding packages for pre-processors (e.g. Pug, SASS, CoffeeScript) to get proper syntax highlighting for them.

### Enabling JSX Highlighting

The `<script>` block uses the syntax highlighting currently active for you normal `.js` files. To support JSX highlighting inside Vue files:

1. Install and set [Babel javascript highlighting package](https://packagecontrol.io/packages/Babel), which supports JSX, as your default JS highlighting.

2. Explicitly disable Sublime's default `JavaScript` package. This allows the Babel package to be applied the embedded `<script>` in `*.vue` files. You may need to restart Sublime for this to take effect.

### Development

- The development of this syntax relies on the [YAML-Macros](https://github.com/Thom1729/YAML-Macros) package. You can install it from Package Control.

- Do not edit `Vue Component.sublime-syntax` directly. Work in `Vue Component.sublime-syntax.yaml-macros` instead. Once done editing, run "Build With: YAML Macros" from Sublime's command palette. This will update the actual `Vue Component.sublime-syntax` file.

### License

[MIT](http://opensource.org/licenses/MIT)
