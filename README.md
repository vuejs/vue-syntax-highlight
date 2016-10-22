# Vue Syntax Highlight

Sublime Text Syntax highlighting for single-file [Vue.js](http://vuejs.org) components (enabled by [vue-loader](https://github.com/vuejs/vue-loader) or [vueify](https://github.com/vuejs/vueify)).

![screenshot](https://cloud.githubusercontent.com/assets/499550/11458853/99ed23aa-9696-11e5-9bf6-43c706487aee.png)

### Install

- Via Package Control: search for `Vue Syntax Highlight`.
- Manual: clone this repo into your Sublime `Packages` folder.

**NOTE:** You still need to install corresponding packages for pre-processors (e.g. Jade, SASS, CoffeeScript) to get proper syntax highlighting for them.

### Enabling JSX Highlighting

The `<script>` block uses the syntax highlighting currently active for you normal `.js` files. To support JSX highlighting inside Vue files, just set [Babel javascript highlighting package](https://packagecontrol.io/packages/Babel), which supports JSX, as your default JS highlighting. **Note you may need to explicitly disable Sublime's default `JavaScript` package to make it work.**

### License

[MIT](http://opensource.org/licenses/MIT)
