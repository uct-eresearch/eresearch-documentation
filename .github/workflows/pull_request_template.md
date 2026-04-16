## Documentation QA checklist

Please confirm before requesting review:

### Structure and boundaries

- [ ] Content fits the correct layer (Task / How-to / Service / Reference / Tutorial)
- [ ] No duplication across sections
- [ ] No discipline-specific content added to core layers (unless in Tutorials)

### Clarity and execution

- [ ] How-to guides are step-by-step and executable
- [ ] Tasks are routing-focused (not instructional)
- [ ] Tutorials link out (do not contain commands or steps)

### Links and navigation

- [ ] All links are relative and working
- [ ] Navigation entries match actual files
- [ ] No orphan pages introduced

### Tone and consistency

- [ ] Language is clear, direct, and minimal
- [ ] No unnecessary explanation or teaching in operational pages
- [ ] No tool-specific detail in the wrong layer

### Build integrity

- [ ] `mkdocs build --strict` passes locally (or via CI)