// SYNTAX TEST "Vue Component.sublime-syntax"

    <template>
// <- text.html.vue - text text
//  ^^^^^^^^^^ meta.tag.template.begin.html

    </template>
// <- text.html.vue - text text
//  ^^^^^^^^^^^ meta.tag.template.end.html


    <template lang="jade"> foo </template>
//  ^^^^^^^^^^^^^^^^^^^^^^ meta.tag - source
//                        ^^^^^ text.jade.embedded.html - meta.tag
//                             ^^^^^^^^^^^ meta.tag - source

    <template lang="jade"> foo --> </template>
//  ^^^^^^^^^^^^^^^^^^^^^^ meta.tag - source
//                        ^^^^^ text.jade.embedded.html - meta.tag
//                             ^^^^ - meta.tag - source
//                             ^^^ comment.block.html punctuation.definition.comment.end.html
//                                 ^^^^^^^^^^^ meta.tag - source

    <template lang="jade"> <!-- foo </template>
//  ^^^^^^^^^^^^^^^^^^^^^^ meta.tag - source
//                        ^^^^^ - meta.tag - source
//                         ^^^^ punctuation.definition.comment.begin.html
//                             ^^^^^ text.jade.embedded.html - meta.tag
//                                  ^^^^^^^^^^^ meta.tag - source

    <template lang="jade"> <!-- foo --> </template>
//  ^^^^^^^^^^^^^^^^^^^^^^ meta.tag - source
//                        ^^^^^ - meta.tag - source
//                         ^^^^ punctuation.definition.comment.begin.html
//                             ^^^^^ text.jade.embedded.html - meta.tag
//                                  ^^^^ - meta.tag - source
//                                  ^^^ comment.block.html punctuation.definition.comment.end.html
//                                      ^^^^^^^^^^^ meta.tag - source


    <template lang="jade">

// <- text.jade.embedded.html

    </template>
// <- text.jade.embedded.html
//^^ text.jade.embedded.html
//  ^^^^^^^^^^^ meta.tag - meta.tag meta.tag - text.jade


    <template lang="jade">
//  ^^^^^^^^^^ meta.tag - meta.tag meta.tag - meta.attribute-with-value
//            ^^^^^^^^^^^ meta.tag meta.attribute-with-value.html - meta.tag meta.tag
//                       ^ meta.tag.template.begin.html - meta.tag meta.tag
//  ^ punctuation.definition.tag.begin.html
//   ^^^^^^^^ entity.name.tag.template.html
//            ^^^^ entity.other.attribute-name.html
//                ^ punctuation.separator.key-value.html
//                       ^ punctuation.definition.tag.end.html
//                        ^ - text.jade

// <- text.jade.embedded.html
    </template>
// <- text.jade.embedded.html
//^^ text.jade.embedded.html
//  ^^^^^^^^^^^ meta.tag - meta.tag meta.tag - text.jade
//  ^^ punctuation.definition.tag.begin.html
//    ^^^^^^^^ entity.name.tag.template.html
//            ^ punctuation.definition.tag.end.html

    <template lang="pug">
//  ^^^^^^^^^^ meta.tag - meta.tag meta.tag - meta.attribute-with-value
//            ^^^^^^^^^^ meta.tag meta.attribute-with-value.html - meta.tag meta.tag
//                      ^ meta.tag.template.begin.html - meta.tag meta.tag
//  ^ punctuation.definition.tag.begin.html
//   ^^^^^^^^ entity.name.tag.template.html
//            ^^^^ entity.other.attribute-name.html
//                ^ punctuation.separator.key-value.html
//                      ^ punctuation.definition.tag.end.html
//                       ^ - text.pug

// <- text.pug.embedded.html
    </template>
// <- text.pug.embedded.html
//^^ text.pug.embedded.html
//  ^^^^^^^^^^^ meta.tag - meta.tag meta.tag - text.pug
//  ^^ punctuation.definition.tag.begin.html
//    ^^^^^^^^ entity.name.tag.template.html
//            ^ punctuation.definition.tag.end.html

    <template lang="slm">
//  ^^^^^^^^^^ meta.tag - meta.tag meta.tag - meta.attribute-with-value
//            ^^^^^^^^^^ meta.tag meta.attribute-with-value.html - meta.tag meta.tag
//                      ^ meta.tag.template.begin.html - meta.tag meta.tag
//  ^ punctuation.definition.tag.begin.html
//   ^^^^^^^^ entity.name.tag.template.html
//            ^^^^ entity.other.attribute-name.html
//                ^ punctuation.separator.key-value.html
//                      ^ punctuation.definition.tag.end.html
//                       ^ - text.slm

// <- text.slm.embedded.html
    </template>
// <- text.slm.embedded.html
//^^ text.slm.embedded.html
//  ^^^^^^^^^^^ meta.tag - meta.tag meta.tag - text.slm
//  ^^ punctuation.definition.tag.begin.html
//    ^^^^^^^^ entity.name.tag.template.html
//            ^ punctuation.definition.tag.end.html
