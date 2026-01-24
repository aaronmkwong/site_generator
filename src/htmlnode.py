
# represent a "node" in an HTML document tree
# (like a <p> tag and its contents, or an <a> tag and its contents)
#  and can be block level or inline, and is designed to only output HTML

class HTMLNode:

    # initialize data members
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # child classes will override this method to render themselves as HTML
    def to_html(self):
        raise NotImplementedError

    # formatted string representing the HTML attributes of the node
    def props_to_html(self):
        if self.props is None or not self.props:
            return ''
        else:
            attrs = ''
            for key in self.props.keys():
                attrs +=  f' {key}="{self.props[key]}"'
            return attrs

    # prints an HTMLNode object for debugging to see its tag, value, children, props
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
