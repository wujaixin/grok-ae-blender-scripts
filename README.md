# Grok AE & Blender Scripts

为 Grok 推荐的 After Effects (AE) 和 Blender 自动化脚本库。

**Repo URL**: https://github.com/wujaixin/grok-ae-blender-scripts

## 目的
- 方便 Grok 读取并推荐最佳 VFX 工作流脚本
- 提供实用批量处理、自动化和项目配置

## 目录结构
- `blender/` - Blender Python 脚本
  - batch_render.py 批量渲染
  - camera_setup.py 85mm 相机设置
- `ae/` - After Effects JSX 脚本
  - import_footage.jsx 导入材料
  - create_comp.jsx 创建组成
- `configs/` - 项目配置
  - blender_settings.txt
  - ae_template.txt

## 如何使用
**Blender**:
1. 打开 Blender
2. Scripting 面板
3. 粘贴脚本运行

**AE**:
1. 将 .jsx 文件放到 AE/Scripts 目录
2. 或 File > Scripts > Run Script File

## Grok 推荐
直接对 Grok 说：“从 grok-ae-blender-scripts 仓库推荐一个 Blender 批量渲染脚本”

**Created for easy Grok integration!**