
installed packages:

* styled-components
* rich-markdown-editor
* markdown-it
* react-is


Peer dependencies:

```yaml
packageExtensions:
  rich-markdown-editor@*:
      peerDependencies:
        react: "*"
        react-dom: "*"
        styled-components: "*"
  styled-components@*:
      peerDependencies:
        react-is: "*"
        markdown-it: "*"
```

Add fallback to webpack configs

```javascript
resolve: {
    ...
    fallback: {
      "punycode": false,
      "assert": false,
    },//fallback
    ...
}
```