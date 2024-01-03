import React from 'react'
import { createRoot } from 'react-dom/client'
import Markdown from 'react-markdown'
import MonacoEditor, { MonacoDiffEditor } from 'react-monaco-editor'
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter'
import { dark } from 'react-syntax-highlighter/dist/esm/styles/prism'
import CodeMirror from '@uiw/react-codemirror';
// import { javascript } from '@codemirror/lang-javascript';

// Did you know you can use tildes instead of backticks for code in markdown? ✨
const markdown = `Here is some JavaScript code:

~~~python
import os
import unitte

class TestReadFile(unittest.TestCase):
    def test_read(self):
        with open(os.path.join(os.path.dirname(__file__), "sample.py"), "r") as file:
            code = file.read()
            code = code.replace("Hello !", "Hello world")
            print(code)

        with open(os.path.join(os.path.dirname(__file__), "sample.py"), "w") as file:
            file.write(code)
~~~
`

export default function MarkDown() {
    return (
        <Markdown
            children={markdown}
            components={{
                code(props) {
                    const { children, className, node, ...rest } = props
                    const match = /language-(\w+)/.exec(className || '')
                    return match ? (
                        <CodeMirror value={String(children).replace(/\n$/, '')} height="200px" />

                        // <SyntaxHighlighter
                        //     // {...rest}
                        //     PreTag="div"
                        //     children={String(children).replace(/\n$/, '')}
                        //     language={match[1]}
                        //     style={dark}
                        // />
                    ) : (
                        <code {...rest} className={className}>
                            {children}
                        </code>
                    )
                }
            }}
        />
    )
}
