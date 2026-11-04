# zen-internet-themes

My custom transparent themes for the [Zen Internet](https://github.com/sameerasw/zen-internet) extension.

`styles.json` = the official theme list + my overrides from `styles/`. A GitHub Action rebuilds it on every push and daily, so official updates still arrive.

## Use it

Zen Internet → data viewer → **Repository URL**:

```
https://raw.githubusercontent.com/Pugmeowla/zen-internet-themes/main/styles.json
```

Then **Refetch styles** and reload the site.

## Add or edit a theme

1. Make `styles/<hostname>/` (e.g. `styles/classroom.google.com/`).
2. Add one `.css` file per toggle. The filename is the toggle name in the popup.
   - Names containing `transparency` are switched off by Zen Internet's "disable transparency" option.
   - `name $ description.css` shows the description in the popup.
3. Push. The Action rebuilds `styles.json`.

Local build: `python3 build.py`.

## Themes

- **classroom.google.com**: light frosted glass, icon-only sidebar that expands on hover, centred pill tabs, pastel class cards and stream header, glass topic cards in Classwork, SF Pro font, blue accent.
