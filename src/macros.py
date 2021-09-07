from YAMLMacros.lib.syntax import rule as _rule

def script_language(match, embed):
    return embed_language_in_tag('script', match, embed)

def style_language(match, embed):
    return embed_language_in_tag('style', match, embed)

def template_language(match, embed):
    return embed_language_in_tag('template', match, embed)

def embed_language_in_tag(tag, match, embed):
    return _rule(
        match=r'(?i)(?={0}{{{{unquoted_attribute_break}}}}|\'{0}\'|"{0}")'.format(match),
        set=[
            [
                _rule(meta_content_scope='meta.tag.%s.begin.html' % tag),
                _rule(include='%s-common' % tag),
                _rule(
                    match='>',
                    scope='punctuation.definition.tag.end.html',
                    set=[
                        [
                            _rule(include='%s-close-tag' % tag)
                        ],
                        [
                            _rule(
                                match=r'{{%s_content_begin}}' % tag,
                                captures={
                                    1: 'comment.block.html punctuation.definition.comment.begin.html',
                                },
                                pop=1,
                                embed=('scope:%s' % embed),
                                embed_scope=('%s.embedded.html' % embed),
                                escape='{{%s_content_end}}' % tag,
                                escape_captures={
                                  1: ('%s.embedded.html' % embed),
                                  2: 'comment.block.html punctuation.definition.comment.end.html',
                                  3: ('%s.embedded.html' % embed),
                                  4: 'comment.block.html punctuation.definition.comment.end.html',
                                },
                            )
                        ]
                    ]
                ),
            ],
            'tag-generic-attribute-meta',
            'tag-generic-attribute-value',
        ]
    )
