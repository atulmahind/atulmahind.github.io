# atma म्हणे

Personal website and blog of Atul Mahind: <https://mahind.in>.

## Deployment settings

| Setting | Value |
| --- | --- |
| Repository | `atulmahind/atulmahind.github.io` |
| Hosting | GitHub Pages |
| Custom domain | `mahind.in`, recorded in `CNAME` |
| Website path | Domain root; empty Jekyll base URL |
| Deployment branch | `master` |
| Workflow | `.github/workflows/pages.yml` |
| Triggers | Push to `master`, or manual **Run workflow** |
| Build runtime | Ruby 3.4 on `ubuntu-latest` |
| Dependencies | Bundler using `Gemfile` (`jekyll-v4-github-pages ~> 232`) |
| Build command | `bundle exec jekyll build --baseurl ""` |
| Build environment | `JEKYLL_ENV=production` |
| Published output | `_site/`, uploaded as a Pages artifact |
| Deployment environment | `github-pages` |
| Authentication | Automatic `GITHUB_TOKEN` and GitHub OIDC; no personal token required |

The branch, repository URL, and domain are recorded from the local repository.
The workflow defines the deployment configuration above. The active GitHub Pages
dashboard settings and DNS configuration have not been verified.

### GitHub setup

1. In the repository's **Settings → Pages → Build and deployment**, select
   **GitHub Actions** as the source.
2. Confirm **Custom domain** is `mahind.in` and enable **Enforce HTTPS** once
   GitHub reports that the domain and certificate are ready. Keep the existing
   DNS records unless GitHub's domain check reports a problem.
3. Ensure repository Actions are enabled and the `github-pages` environment
   permits deployments from `master`. Any environment approval rules still apply.
4. Commit and push the workflow to `master`. Check the **Actions** tab for the
   build and deployment results. Later pushes to `master` deploy automatically.

Manual runs from other branches build the website but skip deployment.
Deployments run one at a time, and an active deployment is allowed to finish.
Only the deploy job receives `pages: write` and `id-token: write` permissions.

`_site/` is generated and ignored by Git. `Gemfile.lock` is currently ignored too,
so CI resolves dependencies from `Gemfile` rather than a committed lockfile.

The workflow follows GitHub's
[Jekyll Pages workflow](https://github.com/actions/starter-workflows/blob/main/pages/jekyll.yml)
using this site's root-domain build settings.

## Local preview

With Ruby 3.4 and Bundler installed:

```sh
bundle install
bundle exec jekyll serve
```

Open <http://localhost:4000>. To check a production build locally:

```sh
JEKYLL_ENV=production bundle exec jekyll build --baseurl ""
```

## Publishing content

### Gallery images

Homepage photographs use responsive WebP variants at 400, 800, and 1110 pixels
wide, with the original JPEGs retained for fallback and full-size links.
After replacing a JPEG in `assets/img/fine-art/`, regenerate the variants:

```sh
python3 -m venv /tmp/gallery-images
/tmp/gallery-images/bin/pip install Pillow==13.0.0
/tmp/gallery-images/bin/python scripts/optimize-gallery.py
```

Keep image dimensions and alternative text in `index.html` in sync with any
replacement. Only the first photograph has high fetch priority; later images
remain lazy-loaded. Fonts are hosted in `assets/fonts/noto-sans-devanagari/`
with their license and source information.

### Posts and pages

Add posts to `_posts/` as `YYYY-MM-DD-slug.md`, using `layout: post` and a
`title` in YAML front matter. The blog archive lists them automatically.
Standalone pages use `layout: page`. Navigation is in `_data/navigation.yml`.

The document language defaults to Marathi (`lang: mr` in `_config.yml`). Set
`lang: en` in a page or post's front matter when its main content is English;
use `lang: mr` for an explicit Marathi override. The shared layout applies
the page setting first, then the site default.
