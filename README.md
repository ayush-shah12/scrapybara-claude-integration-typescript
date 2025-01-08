# About

This repository demonstrates a fully functional interaction loop implemented with the Anthropic TypeScript SDK and Scrapybara TypeScript SDK. 

This can be used to interact with Scrapybara instances through Claude integration like computer use, bash tool, and any customn tool you want, without going through the Agent protocols defined by Scrapybara (which are subject to high cost per call and have no customization for custom tools).

This implementation is similar to the Python loop with some minor changes, but functions identically. 

This was created for a project I'm working on (ScrapyPilot!) and also since Scrapybara doesn't support Claude integration with their Typescript SDK for some reason.

This implementation serves as a practical guide for those seeking to leverage these tools in a TypeScript environment.

# Improvements

- Abstract the running of tools into a new class, possibly implement a ToolCollection class similar to how it's defined in the Python SDK.
- Abstract away creation of custom tools through an interface
