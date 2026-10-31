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

Add posts to `_posts/` as `YYYY-MM-DD-slug.md`, using `layout: post` and a
`title` in YAML front matter. The blog archive lists them automatically.
Standalone pages use `layout: page`. Navigation is in `_data/navigation.yml`.
