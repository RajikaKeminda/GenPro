# GenPro

## Generative AI for professional project management.
GenPro is a simple CLI developed using python and generative AI model (gpt-3.5-turbo-16k).

### What you can do with GenPro:
1. You can ask anything about your project.
2. You can analyze and optimize codes.
3. You can easily create files with generated contents.
4. You can modify existing file contents.
5. You can do whatever you want with your creativity.

### Installation
```
  pip install genpro
```

### Configuration
```
  gen set-key OPENAI_API_KEY
```
or
```
  gp set-key OPENAI_API_KEY
```

### Commands

Ask about your project
```
  gen ask "Explain App.test.ts"
```

Create files
```
  gen create "Create sample navbar using tailwind css."
```

Modify files
```
  gen change "Remove current main page content and place Hello world in middle of the screen. use tailwind css. hint: App.tsx"
```
