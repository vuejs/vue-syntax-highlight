// SYNTAX TEST "Vue Component.sublime-syntax"

    <h1> {{ foo.text }} </h1>
//       ^^^^^^^^^^^^^^ meta.template.vue
//       ^^ punctuation.definition.template.begin.html
//         ^^^^^^^^^^ source.js.embedded.vue
//                   ^^ punctuation.definition.template.end.html

    <p {{foo.attrib}}>
//     ^^^^^^^^^^^^^^ meta.template.vue
//     ^^ punctuation.definition.template.begin.html
//       ^^^^^^^^^^ source.js.embedded.vue
//                 ^^ punctuation.definition.template.end.html

    <p attrib="{{ foo.value }}" >
//            ^ meta.tag meta.attribute-with-value.html meta.string.html - meta.interpolation
//             ^^^^^^^^^^^^^^^ meta.tag meta.attribute-with-value.html meta.string.html meta.interpolation.vue
//                            ^ meta.tag meta.attribute-with-value.html meta.string.html - meta.interpolation
//            ^ string.quoted.double.html punctuation.definition.string.begin.html
//             ^^ punctuation.definition.template.begin.html - source.js
//               ^^^^^^^^^^^ source.js.embedded.vue
//                          ^^ punctuation.definition.template.end.html - source.js
//                            ^ string.quoted.double.html punctuation.definition.string.end.html

    <p attrib='{{ foo.value }}' >
//            ^ meta.tag meta.attribute-with-value.html meta.string.html - meta.interpolation
//             ^^^^^^^^^^^^^^^ meta.tag meta.attribute-with-value.html meta.string.html meta.interpolation.vue
//                            ^ meta.tag meta.attribute-with-value.html meta.string.html - meta.interpolation
//            ^ string.quoted.single.html punctuation.definition.string.begin.html
//             ^^ punctuation.definition.template.begin.html - source.js
//               ^^^^^^^^^^^ source.js.embedded.vue
//                          ^^ punctuation.definition.template.end.html - source.js
//                            ^ string.quoted.single.html punctuation.definition.string.end.html

    <p attrib={{ foo.value }} >
//            ^^^^^^^^^^^^^^^ meta.tag meta.attribute-with-value.html meta.string.html meta.interpolation.vue
//            ^^ punctuation.definition.template.begin.html - source.js
//              ^^^^^^^^^^^ source.js.embedded.vue
//                         ^^ punctuation.definition.template.end.html - source.js

    <p v-attrib="{'key': 'value'}">
//  ^^^ meta.tag - meta.attribute-with-value
//     ^^^^^^^^^ meta.tag meta.attribute-with-value.directive.html - meta.string
//              ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//               ^^^^^^^^^^^^^^^^ meta.tag meta.attribute-with-value.directive.html meta.string.html meta.interpolation.vue source.js.embedded.vue meta.mapping
//                               ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//                                ^ meta.tag - meta.attribute-with-value
//                                 ^ - meta.tag

    <p v-attrib="i = 0">
//  ^^^ meta.tag - meta.attribute-with-value
//     ^^^^^^^^^ meta.tag meta.attribute-with-value.directive.html - meta.string
//              ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//               ^^^^^ meta.tag meta.attribute-with-value.directive.html meta.string.html meta.interpolation.vue source.js.embedded.vue
//                    ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//                     ^ meta.tag - meta.attribute-with-value
//                      ^ - meta.tag

    <p v-attrib='i = 0'>
//  ^^^ meta.tag - meta.attribute-with-value
//     ^^^^^^^^^ meta.tag meta.attribute-with-value.directive.html - meta.string
//              ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//               ^^^^^ meta.tag meta.attribute-with-value.directive.html meta.string.html meta.interpolation.vue source.js.embedded.vue
//                    ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//                     ^ meta.tag - meta.attribute-with-value
//                      ^ - meta.tag

</html>
