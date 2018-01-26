# Vue Syntax Highlight

**Note:** The `master` branch hosts the `tmLanguage` based implementation that is distributed to Sublime Text build < 3153. It is also used to power GitHub's syntax highlight of `*.vue` files in [linguist](https://github.com/github/linguist).

For a newer implementation of the syntax that is distributed to build >=3153, See the [new](https://github.com/vuejs/vue-syntax-highlight/tree/new) branch.

---

Sublime Text Syntax highlighting for single-file [Vue.js](http://vuejs.org) components (enabled by [vue-loader](https://github.com/vuejs/vue-loader) or [vueify](https://github.com/vuejs/vueify)).

![screenshot](https://raw.githubusercontent.com/vuejs/vue-syntax-highlight/new/samples/screenshot.png)

### Install

- Via Package Control: search for `Vue Syntax Highlight`.
- Manual: clone this repo into your Sublime `Packages` folder.

**NOTE:** You still need to install corresponding packages for pre-processors (e.g. Jade, SASS, CoffeeScript) to get proper syntax highlighting for them.

### Enabling JSX Highlighting

The `<script>` block uses the syntax highlighting currently active for you normal `.js` files. To support JSX highlighting inside Vue files, just set [Babel javascript highlighting package](https://packagecontrol.io/packages/Babel), which supports JSX, as your default JS highlighting. **Note you may need to explicitly disable Sublime's default `JavaScript` package to make it work.**

### License

[MIT](http://opensource.org/licenses/MIT)
