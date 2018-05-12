from YAMLMacros.lib.syntax import rule as _rule
from YAMLMacros.lib.extend import *

def script_language(match, embed):
    return embed_language_in_tag('script', match, embed)

def style_language(match, embed):
    return embed_language_in_tag('style', match, embed)

def template_language(match, embed):
    return embed_language_in_tag('template', match, embed)

def embed_language_in_tag(tag, match, embed):
    return _rule(
        match=r'(?i)(?={0}(?!{{{{unquoted_attribute_value}}}})|\'{0}\'|"{0}")'.format(match),
        set=[
            [
                _rule(meta_content_scope='meta.tag.%s.begin.html' % tag),
                _rule(include='%s-common' % tag),
                _rule(
                    match='>',
                    scope='punctuation.definition.tag.end.html',
                    set=[
                        _rule(include='%s-close-tag' % tag),
                        _rule(
                            match=r'',
                            embed=('scope:%s' % embed),
                            embed_scope=('%s.embedded.html' % embed),
                            escape=r'(?i)(?=(?:-->\s*)?</%s)' % tag,
                        )
                    ]
                ),
            ],
            'tag-generic-attribute-meta',
            'tag-generic-attribute-value',
        ]
    )
