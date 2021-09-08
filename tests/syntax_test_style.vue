// SYNTAX TEST "Packages/Vue/Vue Component.sublime-syntax"


    <style> h1 {} </style>
//  ^^^^^^^ meta.tag - source
//         ^^^^^^^ source.css.embedded.html - meta.tag
//                ^^^^^^^^ meta.tag - source

    <style> h1 {} --> </style>
//  ^^^^^^^ meta.tag - source
//         ^^^^^^^ source.css.embedded.html - meta.tag
//                ^^^^ - meta.tag - source
//                ^^^ comment.block.html punctuation.definition.comment.end.html
//                    ^^^^^^^^ meta.tag - source

    <style> <!-- h1 {} </style>
//  ^^^^^^^ meta.tag - source
//         ^^^^^ - meta.tag - source
//              ^^^^^^^ source.css.embedded.html - meta.tag
//                     ^^^^^^^^ meta.tag - source
//          ^^^^ punctuation.definition.comment.begin.html

    <style> <!-- h1 {} --> </style>
//  ^^^^^^^ meta.tag - source
//         ^^^^^ - meta.tag - source
//          ^^^^ punctuation.definition.comment.begin.html
//              ^^^^^^^ source.css.embedded.html - meta.tag
//                     ^^^^ - meta.tag - source
//                     ^^^ comment.block.html punctuation.definition.comment.end.html
//                         ^^^^^^^^ meta.tag - source


    <style>

// <- source.css.embedded.html

    </style>
// <- source.css.embedded.html - source source
// ^ source.css.embedded.html - source source
//  ^^^^^^^^ meta.tag - source


    <style>
    <!--
//^^^^^^ - meta.tag - source
//  ^^^^ comment.block.html punctuation.definition.comment.begin.html
//      ^ source.css.embedded.html - source source - meta.tag - comment
    h1 {}
// ^^^^^^^ source.css.embedded.html - source source - meta.tag
    -->
//^^ source.css.embedded.html - meta.tag - comment
//  ^^^^ - source - meta.tag
//  ^^^ comment.block.html punctuation.definition.comment.end.html
    var i = 0;
// ^^^^^^^^^^^^ - source
    </style>
//  ^^^^^^^^ meta.tag - source


    <style> <!--
//  ^^^^^^^^^^^^ - source
//  ^^^^^^^ meta.tag
//  ^ punctuation.definition.tag.begin.html
//   ^^^^^ entity.name.tag
//        ^ punctuation.definition.tag.end.html
//         ^ - meta.tag - comment
//          ^^^^ comment.block.html punctuation.definition.comment.begin.html
//              ^ source.css.embedded.html - source source

    h1 {}
// <- source.css.embedded.html - source source

    --> </style>
// ^ source.css.embedded.html - source source
//  ^^^^^^^^^^^^^ - source
//     ^ - meta.tag - comment
//      ^^^^^^^^ meta.tag
//              ^ - meta.tag
//  ^^^ comment.block.html punctuation.definition.comment.end.html
//      ^^ punctuation.definition.tag.begin.html
//        ^^^^^ entity.name.tag
//             ^ punctuation.definition.tag.end.html


    <style type="text/css"> <!--
//  ^^^^^^^ meta.tag - meta.tag meta.tag - meta.attribute-with-value - source
//         ^^^^^^^^^^^^^^^ meta.tag meta.attribute-with-value.html - meta.tag meta.tag - meta.attribute-with-value meta.attribute-with-value - source
//                        ^ meta.tag - meta.tag meta.tag - meta.attribute-with-value - source
//                         ^^^^^ - meta.tag - source
//   ^^^^^ entity.name.tag
//         ^^^^ entity.other.attribute-name.html
//             ^ punctuation.separator.key-value.html
//              ^^^^^^^^^^ string.quoted.double.html
//                          ^^^^ comment.block.html punctuation.definition.comment.begin.html
//                              ^ source.css.embedded.html

    h1 {}
// <- source.css.embedded.html - source source

    --> </style>
// ^ source.css.embedded.html - source source
//  ^^^^^^^^^^^^^ - source
//     ^ - meta.tag - comment
//      ^^^^^^^^ meta.tag
//              ^ - meta.tag
//  ^^^ comment.block.html punctuation.definition.comment.end.html
//      ^^ punctuation.definition.tag.begin.html
//        ^^^^^ entity.name.tag
//             ^ punctuation.definition.tag.end.html


    <style
    type
//  ^^^^ meta.tag meta.attribute-with-value.html - meta.tag meta.tag - meta.attribute-with-value meta.attribute-with-value
    =
    tExT/cSs>
//  ^^^^^^^^ meta.tag meta.attribute-with-value.html - meta.tag meta.tag - meta.attribute-with-value meta.attribute-with-value

    h1 {}
// <- source.css.embedded.html - source source

    </style>
// <- source.css.embedded.html - source source
// ^ source.css.embedded.html - source source
//  ^^^^^^^^ meta.tag - source


    <style lang="less">  </style>
//  ^^^^^^^^^^^^^^^^^^^ meta.tag - meta.tag meta.tag - source
//         ^^^^^^^^^^^ meta.attribute-with-value.html - meta.attribute-with-value meta.attribute-with-value
//                     ^^ source.less.embedded.html - meta.tag
//                       ^^^^^^^^ meta.tag - source


    <style lang="less">

// <- source.less.embedded.html - source source
    </style>
// <- source.less.embedded.html - source source
//^^ source.less.embedded.html - source source
//  ^^^^^^^^ meta.tag - source

    <style lang="less">
        <!--
// ^^^^^^^^^ - source
//      ^^^^ comment.block.html punctuation.definition.comment.begin.html
//          ^ source.less.embedded.html - source source
        -->
// ^^^^^ source.less.embedded.html - source source
//      ^^^ comment.block.html punctuation.definition.comment.end.html - source
//         ^ - source - comment - meta.tag
    </style>
// <- - source - comment - meta.tag
//^^ - source - comment - meta.tag
//  ^^^^^^^^ meta.tag - source


    <style lang="postcss">

// <- source.postcss.embedded.html - source source
    </style>
// <- source.postcss.embedded.html - source source
//^^ source.postcss.embedded.html - source source
//  ^^^^^^^^ meta.tag - source

    <style lang="postcss">
        <!--
// ^^^^^^^^^ - source
//      ^^^^ comment.block.html punctuation.definition.comment.begin.html
//          ^ source.postcss.embedded.html - source source
        -->
// ^^^^^ source.postcss.embedded.html - source source
//      ^^^ comment.block.html punctuation.definition.comment.end.html - source
//         ^ - source - comment - meta.tag
    </style>
// <- - source - comment - meta.tag
//^^ - source - comment - meta.tag
//  ^^^^^^^^ meta.tag - source


    <style lang="postcss?parser=sugarss">

// <- source.sss.embedded.html - source source
    </style>
// <- source.sss.embedded.html - source source
//^^ source.sss.embedded.html - source source
//  ^^^^^^^^ meta.tag - source

    <style lang="postcss?parser=sugarss">
        <!--
// ^^^^^^^^^ - source
//      ^^^^ comment.block.html punctuation.definition.comment.begin.html
//          ^ source.sss.embedded.html - source source
        -->
// ^^^^^ source.sss.embedded.html - source source
//      ^^^ comment.block.html punctuation.definition.comment.end.html - source
//         ^ - source - comment - meta.tag
    </style>
// <- - source - comment - meta.tag
//^^ - source - comment - meta.tag
//  ^^^^^^^^ meta.tag - source


    <style lang="sass">

// <- source.sass.embedded.html - source source
    </style>
// <- source.sass.embedded.html - source source
//^^ source.sass.embedded.html - source source
//  ^^^^^^^^ meta.tag - source

    <style lang="sass">
        <!--
// ^^^^^^^^^ - source
//      ^^^^ comment.block.html punctuation.definition.comment.begin.html
//          ^ source.sass.embedded.html - source source
        -->
// ^^^^^ source.sass.embedded.html - source source
//      ^^^ comment.block.html punctuation.definition.comment.end.html - source
//         ^ - source - comment - meta.tag
    </style>
// <- - source - comment - meta.tag
//^^ - source - comment - meta.tag
//  ^^^^^^^^ meta.tag - source


    <style lang="scss">

// <- source.scss.embedded.html - source source
    </style>
// <- source.scss.embedded.html - source source
//^^ source.scss.embedded.html - source source
//  ^^^^^^^^ meta.tag - source

    <style lang="scss">
        <!--
// ^^^^^^^^^ - source
//      ^^^^ comment.block.html punctuation.definition.comment.begin.html
//          ^ source.scss.embedded.html - source source
        -->
// ^^^^^ source.scss.embedded.html - source source
//      ^^^ comment.block.html punctuation.definition.comment.end.html - source
//         ^ - source - comment - meta.tag
    </style>
// <- - source - comment - meta.tag
//^^ - source - comment - meta.tag
//  ^^^^^^^^ meta.tag - source
