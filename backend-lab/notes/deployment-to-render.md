# Deployments to Rebder Notes
## Week 1
## Date: June 14th, 2026
### 1. What I did today
```
Deployed my two Academic Projects to Render using Github Actions to automate CI/CD workflows
```
 
### 2. Render Deployment Troubleshooting

**Build Command for TypeScript Projects**
- Use the following command for TypeScript projects:
  ```
  npm install && npm run build
  ```
- The **Start Command** must point to your compiled output file.
  - Example: `node dist/app.js` or `npm start`

**Common Issues & Solutions**
- **Missing `dist/` folder:**
  - Indicates the build failed locally.
  - **Solution:** Always run `npm run build` before pushing your code.
- **Error: `Cannot find module dist/app.js`:**
  - TypeScript did not compile, or the output path is incorrect.
- **SQLite / bcrypt errors:**
  - These arise from native dependency mismatches between your local machine and Render's Linux environment.
  - **Solution:** Try downgrading the dependency version or switching to a different library.
- **Hardcoded Ports:**
  - Always use `process.env.PORT` provided by Render. Do **not** hardcode port 3000.

**General Tips**
- Deployments update automatically after a `git push`.