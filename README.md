# GenPro

## Generative AI for professional project management.
GenPro is a simple CLI developed using python and generative AI model (gpt-3.5-turbo-16k).

### What you can do with GenPro:
1. You can ask anything about your project and get rich data visualization in console.
2. You can analyze and optimize codes.
3. You can easily create files with generated contents.
4. You can modify existing file contents.
5. You can do whatever you want with your creativity.

## Short videos:

Creating and modifying components.

https://github.com/RajikaKeminda/GenPro/assets/41231001/bc4fd5c1-36a9-4800-9e63-11776ad59fa4


https://github.com/RajikaKeminda/GenPro/assets/41231001/057e6647-2914-42b2-a21e-4833a4d4a0ab


Ask for an explanation.

https://github.com/RajikaKeminda/GenPro/assets/41231001/726f0d7a-1c5f-49b0-a17d-05016c4e5d06


## Installation
```
  pip install genpro
```

## Configuration
```
  gen set-key OPENAI_API_KEY
```
or
```
  gp set-key OPENAI_API_KEY
```

## Commands
``Note: Use these commands in your project directory``

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

## Tested OS
macOS 14 Sonoma, Ubuntu
