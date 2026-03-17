# Git 拉取和推送命令

## 拉取 - 从远程获取代码到本地

```bash
# 拉取并合并远程分支到当前分支
git pull origin 分支名

# 常用简写（已设置上游分支时）
git pull

# 只获取不合并
git fetch origin
```

## 推送 - 从本地推送到远程

```bash
# 推送当前分支到远程
git push origin 分支名

# 常用简写（已设置上游分支时）
git push

# 首次推送并设置上游分支
git push -u origin 分支名

# 强制推送（慎用！会覆盖远程内容）
git push -f origin 分支名
```

## 完整工作流程示例

```bash
# 1. 查看当前状态
git status

# 2. 添加修改的文件
git add .

# 3. 提交
git commit -m "提交说明"

# 4. 拉取最新代码（推送前先拉取）
git pull origin main

# 5. 推送到远程
git push origin main
```

## 常见问题处理

```bash
# 推送被拒绝时（远程有新提交）
git pull origin main --rebase
git push origin main

# 查看远程分支
git branch -r
```

## 克隆仓库

```bash
# HTTPS方式克隆
git clone https://github.com/用户名/仓库名.git

# SSH方式克隆（推荐）
git clone git@github.com:用户名/仓库名.git

# 克隆到指定目录
git clone https://github.com/用户名/仓库名.git 目标目录名
```

## 其他常用命令

```bash
# 查看远程仓库信息
git remote -v

# 获取远程更新但不合并
git fetch origin

# 查看本地和远程的差异
git diff main origin/main
```
