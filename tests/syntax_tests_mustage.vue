// SYNTAX TEST "Vue Component.sublime-syntax"

    <h1> {{ foo.text }} </h1>
//       ^^^^^^^^^^^^^^ meta.interpolation.vue
//       ^^ punctuation.section.interpolation.begin.html
//         ^^^^^^^^^^ source.js.embedded.vue
//                   ^^ punctuation.section.interpolation.end.html

    <p {{foo.attrib}}>
//     ^^^^^^^^^^^^^^ meta.interpolation.vue
//     ^^ punctuation.section.interpolation.begin.html
//       ^^^^^^^^^^ source.js.embedded.vue
//                 ^^ punctuation.section.interpolation.end.html

    <p attrib="{{ foo.value }}" >
//            ^ meta.tag meta.attribute-with-value.html meta.string.html - meta.interpolation
//             ^^^^^^^^^^^^^^^ meta.tag meta.attribute-with-value.html meta.string.html meta.interpolation.vue
//                            ^ meta.tag meta.attribute-with-value.html meta.string.html - meta.interpolation
//            ^ string.quoted.double.html punctuation.definition.string.begin.html
//             ^^ punctuation.section.interpolation.begin.html - source.js
//               ^^^^^^^^^^^ source.js.embedded.vue
//                          ^^ punctuation.section.interpolation.end.html - source.js
//                            ^ string.quoted.double.html punctuation.definition.string.end.html

    <p attrib='{{ foo.value }}' >
//            ^ meta.tag meta.attribute-with-value.html meta.string.html - meta.interpolation
//             ^^^^^^^^^^^^^^^ meta.tag meta.attribute-with-value.html meta.string.html meta.interpolation.vue
//                            ^ meta.tag meta.attribute-with-value.html meta.string.html - meta.interpolation
//            ^ string.quoted.single.html punctuation.definition.string.begin.html
//             ^^ punctuation.section.interpolation.begin.html - source.js
//               ^^^^^^^^^^^ source.js.embedded.vue
//                          ^^ punctuation.section.interpolation.end.html - source.js
//                            ^ string.quoted.single.html punctuation.definition.string.end.html

    <p attrib={{ foo.value }} >
//            ^^^^^^^^^^^^^^^ meta.tag meta.attribute-with-value.html meta.string.html meta.interpolation.vue
//            ^^ punctuation.section.interpolation.begin.html - source.js
//              ^^^^^^^^^^^ source.js.embedded.vue
//                         ^^ punctuation.section.interpolation.end.html - source.js

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

    <p @handler="function_call($event)">
//  ^^^ meta.tag - meta.attribute-with-value
//     ^^^^^^^^^ meta.tag meta.attribute-with-value.directive.html - meta.string
//     ^ punctuation.definition.attribute.html
//              ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//               ^^^^^^^^^^^^^^^^^^^^^ meta.tag meta.attribute-with-value.directive.html meta.string.html meta.interpolation.vue source.js.embedded.vue
//                                    ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//                                     ^ meta.tag - meta.attribute-with-value
//                                      ^ - meta.tag

    <p @handler='function_call($event)'>
//  ^^^ meta.tag - meta.attribute-with-value
//     ^^^^^^^^^ meta.tag meta.attribute-with-value.directive.html - meta.string
//     ^ punctuation.definition.attribute.html
//              ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//               ^^^^^^^^^^^^^^^^^^^^^ meta.tag meta.attribute-with-value.directive.html meta.string.html meta.interpolation.vue source.js.embedded.vue
//                                    ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//                                     ^ meta.tag - meta.attribute-with-value
//                                      ^ - meta.tag

    <p #handler="variable">
//  ^^^ meta.tag - meta.attribute-with-value
//     ^^^^^^^^^ meta.tag meta.attribute-with-value.directive.html - meta.string
//     ^ punctuation.definition.attribute.html
//              ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//               ^^^^^^^^ meta.tag meta.attribute-with-value.directive.html meta.string.html meta.interpolation.vue source.js.embedded.vue
//                       ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//                        ^ meta.tag - meta.attribute-with-value
//                         ^ - meta.tag

    <p #handler='variable'>
//  ^^^ meta.tag - meta.attribute-with-value
//     ^^^^^^^^^ meta.tag meta.attribute-with-value.directive.html - meta.string
//     ^ punctuation.definition.attribute.html
//              ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//               ^^^^^^^^ meta.tag meta.attribute-with-value.directive.html meta.string.html meta.interpolation.vue source.js.embedded.vue
//                       ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//                        ^ meta.tag - meta.attribute-with-value
//                         ^ - meta.tag

    <p :handler="expression">
//  ^^^ meta.tag - meta.attribute-with-value
//     ^^^^^^^^^ meta.tag meta.attribute-with-value.directive.html - meta.string
//     ^ punctuation.definition.attribute.html
//              ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//               ^^^^^^^^^^ meta.tag meta.attribute-with-value.directive.html meta.string.html meta.interpolation.vue source.js.embedded.vue
//                         ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//                          ^ meta.tag - meta.attribute-with-value
//                           ^ - meta.tag

    <p :handler='expression'>
//  ^^^ meta.tag - meta.attribute-with-value
//     ^^^^^^^^^ meta.tag meta.attribute-with-value.directive.html - meta.string
//     ^ punctuation.definition.attribute.html
//              ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//               ^^^^^^^^^^ meta.tag meta.attribute-with-value.directive.html meta.string.html meta.interpolation.vue source.js.embedded.vue
//                         ^ meta.tag meta.attribute-with-value.directive.html meta.string.html - meta.interpolation
//                          ^ meta.tag - meta.attribute-with-value
//                           ^ - meta.tag

    <template #[`content-${variable}`]>
//            ^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag meta.attribute-with-value.directive.html
//            ^ entity.other.attribute-name.html
//             ^ meta.interpolation.vue punctuation.section.interpolation.begin.vue - source.js.embedded
//              ^^^^^^^^^^^^^^^^^^^^^ meta.interpolation.vue source.js.embedded.vue - entity.other.attribute-name.html
//                                   ^ meta.interpolation.vue punctuation.section.interpolation.end.vue - source.js.embedded
//                                    ^ meta.tag - meta.attribute-with-value
//                                     ^ - meta.tag

    <template v-slot:[`content-${variable}`] >
//            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag meta.attribute-with-value.directive.html
//            ^^^^^^^ entity.other.attribute-name.html
//                   ^ meta.interpolation.vue punctuation.section.interpolation.begin.vue - source.js.embedded
//                    ^^^^^^^^^^^^^^^^^^^^^ meta.interpolation.vue source.js.embedded.vue - entity.other.attribute-name.html
//                                         ^ meta.interpolation.vue punctuation.section.interpolation.end.vue - source.js.embedded
//                                          ^ meta.tag - meta.interpolation
//                                           ^ meta.tag - meta.attribute-with-value
//                                            ^ - meta.tag

</html>
