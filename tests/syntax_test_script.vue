// SYNTAX TEST "Packages/Vue/Vue Component.sublime-syntax"


    <script> var i = 0; </script>
//  ^^^^^^^^ meta.tag - source
//          ^^^^^^^^^^^^ source.js.embedded.html - meta.tag
//                      ^^^^^^^^^ meta.tag - source

    <script> var i = 0; --> </script>
//  ^^^^^^^^ meta.tag - source
//          ^^^^^^^^^^^^ source.js.embedded.html - meta.tag
//                      ^^^^ - meta.tag - source
//                      ^^^ comment.block.html punctuation.definition.comment.end.html
//                          ^^^^^^^^^ meta.tag - source

    <script> <!-- var i = 0; </script>
//  ^^^^^^^^ meta.tag - source
//          ^^^^^ - meta.tag - source
//               ^^^^^^^^^^^^ source.js.embedded.html - meta.tag
//                           ^^^^^^^^^ meta.tag - source
//           ^^^^ punctuation.definition.comment.begin.html

    <script> <!-- var i = 0; --> </script>
//  ^^^^^^^^ meta.tag - source
//          ^^^^^ - meta.tag - source
//           ^^^^ punctuation.definition.comment.begin.html
//               ^^^^^^^^^^^^ source.js.embedded.html - meta.tag
//                           ^^^^ - meta.tag - source
//                           ^^^ comment.block.html punctuation.definition.comment.end.html
//                               ^^^^^^^^^ meta.tag - source


    <script>

// <- source.js.embedded.html
    var i = 0;
// ^^^^^^^^^^^^ source.js.embedded.html - source source
    </script>
// <- source.js.embedded.html - source source
// ^ source.js.embedded.html - source source
//  ^^^^^^^^^ meta.tag - source


    <script>
    <!--
//^^^^^^ - meta.tag - source
//  ^^^^ comment.block.html punctuation.definition.comment.begin.html
//      ^ source.js.embedded.html - source source - meta.tag - comment
    var i = 0;
// ^^^^^^^^^^^^ source.js.embedded.html - source source - meta.tag
    -->
//^^ source.js.embedded.html - meta.tag - comment
//  ^^^^ - source - meta.tag
//  ^^^ comment.block.html punctuation.definition.comment.end.html
    var i = 0;
// ^^^^^^^^^^^^ - source
    </script>
//  ^^^^^^^^^ meta.tag - source


    <script> <!--
//  ^^^^^^^^^^^^^ - source
//  ^^^^^^^^ meta.tag
//  ^ punctuation.definition.tag.begin.html
//   ^^^^^^ entity.name.tag
//         ^ punctuation.definition.tag.end.html
//          ^ - meta.tag - comment
//           ^^^^ comment.block.html punctuation.definition.comment.begin.html
//               ^ source.js.embedded.html - source source

    var foo = 100;
// <- source.js.embedded.html - source source

    (a --> b);
//     ^^^ source.js.embedded.html keyword.operator - comment

    --> </script>
// ^ source.js.embedded.html - source source
//  ^^^^^^^^^^^^^^ - source
//     ^ - meta.tag - comment
//      ^^^^^^^^^ meta.tag
//               ^ - meta.tag
//  ^^^ comment.block.html punctuation.definition.comment.end.html
//      ^^ punctuation.definition.tag.begin.html
//        ^^^^^^ entity.name.tag
//              ^ punctuation.definition.tag.end.html


    <script type="text/javascript"> <!--
//  ^^^^^^^^ meta.tag - meta.tag meta.tag - meta.attribute-with-value - source
//          ^^^^^^^^^^^^^^^^^^^^^^ meta.tag meta.attribute-with-value.html - meta.tag meta.tag - meta.attribute-with-value meta.attribute-with-value - source
//                                ^ meta.tag - meta.tag meta.tag - meta.attribute-with-value - source
//                                 ^^^^^ - meta.tag - source
//   ^^^^^^ entity.name.tag
//          ^^^^ entity.other.attribute-name.html
//              ^ punctuation.separator.key-value.html
//               ^^^^^^^^^^^^^^^^^ string.quoted.double.html
//                                  ^^^^ comment.block.html punctuation.definition.comment.begin.html
//                                      ^ source.js.embedded.html

    var foo = 100;
// <- source.js.embedded.html - source source

    (a --> b);
//     ^^^ source.js.embedded.html keyword.operator - comment

    --> </script>
// ^ source.js.embedded.html - source source
//  ^^^^^^^^^^^^^^ - source
//     ^ - meta.tag - comment
//      ^^^^^^^^^ meta.tag
//               ^ - meta.tag
//  ^^^ comment.block.html punctuation.definition.comment.end.html
//      ^^ punctuation.definition.tag.begin.html
//        ^^^^^^ entity.name.tag
//              ^ punctuation.definition.tag.end.html


    <script
    type
//  ^^^^ meta.tag meta.attribute-with-value.html - meta.tag meta.tag - meta.attribute-with-value meta.attribute-with-value
    =
    application/jAvAsCrIpT>
//  ^^^^^^^^^^^^^^^^^^^^^^ meta.tag meta.attribute-with-value.html - meta.tag meta.tag - meta.attribute-with-value meta.attribute-with-value
    var foo = 100;
// <- source.js.embedded.html - source source
// ^^^^^^^^^^^^^^^^ source.js.embedded.html - source source
    </script>
// <- source.js.embedded.html - source source
// ^ source.js.embedded.html - source source
//  ^^^^^^^^^ meta.tag - source


    <script lang="coffee">

// <- source.coffee.embedded.html - source source
    </script>
// <- source.coffee.embedded.html - source source
//^^ source.coffee.embedded.html - source source
//  ^^^^^^^^^ meta.tag - source

    <script lang="coffee">
        <!--
// ^^^^^^^^^ - source
//      ^^^^ comment.block.html punctuation.definition.comment.begin.html
//          ^ source.coffee.embedded.html - source source
        -->
// ^^^^^ source.coffee.embedded.html - source source
//      ^^^ comment.block.html punctuation.definition.comment.end.html - source
//         ^ - source - comment - meta.tag
    </script>
// <- - source - comment - meta.tag
//^^ - source - comment - meta.tag
//  ^^^^^^^^^ meta.tag - source


    <script lang="livescript">

// <- source.livescript.embedded.html - source source
    </script>
// <- source.livescript.embedded.html - source source
//^^ source.livescript.embedded.html - source source
//  ^^^^^^^^^ meta.tag - source

    <script lang="livescript">
        <!--
// ^^^^^^^^^ - source
//      ^^^^ comment.block.html punctuation.definition.comment.begin.html
//          ^ source.livescript.embedded.html - source source
        -->
// ^^^^^ source.livescript.embedded.html - source source
//      ^^^ comment.block.html punctuation.definition.comment.end.html - source
//         ^ - source - comment - meta.tag
    </script>
// <- - source - comment - meta.tag
//^^ - source - comment - meta.tag
//  ^^^^^^^^^ meta.tag - source


    <script lang="ts">

// <- source.ts.embedded.html - source source
    </script>
// <- source.ts.embedded.html - source source
//^^ source.ts.embedded.html - source source
//  ^^^^^^^^^ meta.tag - source

    <script lang="ts">
        <!--
// ^^^^^^^^^ - source
//      ^^^^ comment.block.html punctuation.definition.comment.begin.html
//          ^ source.ts.embedded.html - source source
        -->
// ^^^^^ source.ts.embedded.html - source source
//      ^^^ comment.block.html punctuation.definition.comment.end.html - source
//         ^ - source - comment - meta.tag
    </script>
// <- - source - comment - meta.tag
//^^ - source - comment - meta.tag
//  ^^^^^^^^^ meta.tag - source
