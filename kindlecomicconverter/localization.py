# -*- coding: utf-8 -*-

import os
from functools import lru_cache

from PySide6.QtCore import QLocale


_TRANSLATIONS_ZH = {
    'Other': '其他',
    'PDF (200MB limit)': 'PDF（200MB 限制）',
    'KFX (does not work)': 'KFX（不可用）',
    'EPUB (200MB limit)': 'EPUB（200MB 限制）',
    'MOBI + EPUB (200MB limit)': 'MOBI + EPUB（200MB 限制）',
    'README': '说明',
    'YOUTUBE': '视频',
    'COMMISSIONS': '委托',
    'DONATE': '捐助',
    'FORUM': '论坛',
    'Select default output folder': '选择默认输出文件夹',
    'Select output directory': '选择输出目录',
    'Select file': '选择文件',
    'Select input folder(s)': '选择输入文件夹',
    'Select directory': '选择目录',
    'Comic (*.cbz *.cbr *.cb7 *.zip *.rar *.7z *.pdf);;All (*.*)':
        '漫画文件 (*.cbz *.cbr *.cb7 *.zip *.rar *.7z *.pdf);;所有文件 (*.*)',
    'Comic (*.pdf);;All (*.*)': '漫画文件 (*.pdf);;所有文件 (*.*)',
    'Comic (*.cbz *.cbr *.cb7)': '漫画文件 (*.cbz *.cbr *.cb7)',
    'Convert': '转换',
    'Abort': '中止',
    'Kindle Comic Converter': 'Kindle Comic Converter',
    'KCC - Error': 'KCC - 错误',
    'KCC - Question': 'KCC - 确认',
    'Gamma: Auto': '伽马：自动',
    'Gamma: {value}': '伽马：{value}',
    'Cropping Power: {value}': '裁剪强度：{value}',
    '<a href="{url}"><b>The new version is available!</b></a>':
        '<a href="{url}"><b>发现新版本！</b></a>',
    '{days} day(s) left': '剩余 {days} 天',
    ' [referral]': ' [推广链接]',
    '<b>Conversion interrupted.</b>': '<b>转换已中断。</b>',
    'Conversion interrupted.': '转换已中断。',
    'Attempting file fusion': '正在尝试合并文件',
    'Created fusion at {path}': '已创建合并文件：{path}',
    'Fusion Failed. {error}': '文件合并失败。{error}',
    "Process Failed. Custom title can't be set when processing more than 1 source.\nDid you forget to check fusion?":
        '处理失败。处理多个来源时不能设置自定义标题。\n你是不是忘记勾选文件合并了？',
    '<b>{progress}Source:</b> {job}': '<b>{progress}来源：</b> {job}',
    'Creating CBZ files': '正在创建 CBZ 文件',
    'Creating PDF files': '正在创建 PDF 文件',
    'Creating EPUB files': '正在创建 EPUB 文件',
    'Creating CBZ files... <b>Done!</b>': '创建 CBZ 文件... <b>完成！</b>',
    'Creating PDF files... <b>Done!</b>': '创建 PDF 文件... <b>完成！</b>',
    'Creating EPUB files... <b>Done!</b>': '创建 EPUB 文件... <b>完成！</b>',
    'Creating MOBI files': '正在创建 MOBI 文件',
    'Creating MOBI files... <b>Done!</b>': '创建 MOBI 文件... <b>完成！</b>',
    'Processing MOBI files': '正在处理 MOBI 文件',
    'Processing MOBI files... <b>Done!</b>': '处理 MOBI 文件... <b>完成！</b>',
    'Kindle detected. Uploading covers... <b>Done!</b>': '检测到 Kindle，正在上传封面... <b>完成！</b>',
    'Failed to process MOBI file!': '处理 MOBI 文件失败！',
    'KindleGen failed to create MOBI!': 'KindleGen 创建 MOBI 失败！',
    'Created EPUB file was too big. Weird file structure?': '生成的 EPUB 文件过大，可能是文件结构异常？',
    'EPUB file: {size}MB. Supported size: ~350MB.': 'EPUB 文件：{size}MB。建议大小约为 350MB。',
    'Unknown Windows error. Possibly filepath too long?': '未知 Windows 错误，可能是文件路径过长？',
    '<b>All jobs completed.</b>': '<b>全部任务已完成。</b>',
    'All jobs completed.': '全部任务已完成。',
    'Cannot select Kindle as output directory': '不能将 Kindle 设备目录选为输出目录',
    'You can choose a taller device profile to get taller cuts in webtoon mode.':
        '在条漫模式下，你可以选择更高的设备配置，以获得更高的切图。',
    'Try reading webtoon panels side by side in landscape!':
        '也可以试试横屏并排阅读条漫分镜！',
    'This option is intended for older Kindle models.':
        '这个选项主要面向较旧的 Kindle 机型。',
    'On this device, there will be conversion speed and quality issues.':
        '在当前设备上，这个选项可能会带来转换速度和画质问题。',
    'Use the Kindle Scribe profile if you want higher resolution when zooming.':
        '如果你希望缩放时有更高分辨率，建议使用 Kindle Scribe 配置。',
    'Scribe PNG MOBI/EPUB has a lot of problems like blank pages/sections. Use JPG instead.':
        'Scribe 的 PNG MOBI/EPUB 容易出现空白页或空白章节，建议改用 JPG。',
    'Colorsoft MOBI/EPUB can have blank pages. Just go back a few pages, exit, and reenter book.':
        'Colorsoft 的 MOBI/EPUB 可能出现空白页。通常后退几页、退出并重新进入即可恢复。',
    '<a href="https://github.com/ciromattia/kcc/wiki/NonKindle-devices">List of supported Non-Kindle devices.</a>':
        '<a href="https://github.com/ciromattia/kcc/wiki/NonKindle-devices">查看支持的非 Kindle 设备列表。</a>',
    "Partially check W/B Margins if you don't want KCC to extend the image margins.":
        '如果你不希望 KCC 自动扩展图片边距，请将“黑/白边距”设为半选。',
    'Error during conversion! Please consult <a href="https://github.com/ciromattia/kcc/wiki/Error-messages">wiki</a> for more details.':
        '转换时发生错误！更多信息请查看 <a href="https://github.com/ciromattia/kcc/wiki/Error-messages">Wiki</a>。',
    'Error during conversion!': '转换时发生错误！',
    'The process will be interrupted. Please wait.': '转换将被中断，请稍候。',
    'No files selected! Please choose files to convert.': '尚未选择文件，请先添加要转换的文件。',
    'Target resolution is not set!': '目标分辨率未设置！',
    '<a href="https://github.com/ciromattia/kcc#kindlegen"><b>Install KindleGen (link)</b></a> to enable MOBI conversion for Kindles!':
        '<a href="https://github.com/ciromattia/kcc#kindlegen"><b>安装 KindleGen（链接）</b></a> 以启用 Kindle 的 MOBI 转换！',
    'Unsupported file type for {path}': '不支持的文件类型：{path}',
    'Your <a href="https://www.amazon.com/b?node=23496309011">KindleGen</a> is outdated! MOBI conversion might fail.':
        '你的 <a href="https://www.amazon.com/b?node=23496309011">KindleGen</a> 版本过旧，MOBI 转换可能失败。',
    '<b>Tip:</b> Hover mouse over options to see additional information in tooltips.':
        '<b>提示：</b>将鼠标悬停在选项上可查看更多说明。',
    '<b>Tip:</b> You can drag and drop image folders or comic files/archives into this window to convert.':
        '<b>提示：</b>你可以直接把图片文件夹或漫画文件/压缩包拖到这个窗口中进行转换。',
    'Since you are a new user of <b>KCC</b> please see few <a href="https://github.com/ciromattia/kcc/wiki/Important-tips">important tips</a>.':
        '你似乎是 <b>KCC</b> 的新用户，建议先查看几条<a href="https://github.com/ciromattia/kcc/wiki/Important-tips">重要提示</a>。',
    '<a href="https://github.com/ciromattia/kcc#7-zip">Install 7z (link)</a> to enable CBZ/CBR/ZIP/etc processing.':
        '<a href="https://github.com/ciromattia/kcc#7-zip">安装 7z（链接）</a> 以启用 CBZ/CBR/ZIP 等格式处理。',
    'Editor is disabled due to a lack of 7z.': '由于缺少 7z，元数据编辑器不可用。',
    '<a href="https://github.com/ciromattia/kcc#7-zip">Install 7z (link)</a> to enable metadata editing.':
        '<a href="https://github.com/ciromattia/kcc#7-zip">安装 7z（链接）</a> 以启用元数据编辑。',
    'CBR metadata are read-only.': 'CBR 元数据为只读。',
    'Separate authors with a comma.': '多个作者请用逗号分隔。',
    '{field} field must be a number.': '{field} 字段必须是数字。',
    'Failed to parse metadata!\n\n{error}\n\nTraceback:\n{traceback}':
        '解析元数据失败！\n\n{error}\n\n回溯：\n{traceback}',
    'Failed to save metadata!\n\n{error}\n\nTraceback:\n{traceback}':
        '保存元数据失败！\n\n{error}\n\n回溯：\n{traceback}',
    'Error during conversion {job}:\n\n{error}\n\nTraceback:\n{traceback}':
        '转换出错 {job}：\n\n{error}\n\n回溯：\n{traceback}',
    'KindleGen error:\n\n{error}': 'KindleGen 错误：\n\n{error}',
}

_BACKEND_WARNING_TRANSLATIONS_ZH = {
    'Put images into folder and drag and drop folder into KCC window.':
        '请将图片放入文件夹后，再把该文件夹拖入 KCC 窗口。',
    'Conversion interrupted.': '转换已中断。',
    'C2P: Source directory is empty.': 'C2P：源目录为空。',
    'Provided input is not a directory.': '提供的输入不是目录。',
    'Target height is not set.': '目标高度未设置。',
    'C2E: Source directory is empty.': 'C2E：源目录为空。',
    'mupdf_pdf_extract_page_image() function can be used only with single image pages.':
        'mupdf_pdf_extract_page_image() 只能用于单图页面。',
    'Not enough disk space to perform conversion.': '磁盘空间不足，无法执行转换。',
    'Failed to prepare a workspace.': '准备工作目录失败。',
    'Failed to extract images from PDF file.': '从 PDF 提取图片失败。',
    'Failed to open source file/directory.': '打开源文件或目录失败。',
    'No images detected, nested archives are not supported.': '未检测到图片，不支持嵌套压缩包。',
    'Unsupported directory structure.': '不支持当前目录结构。',
    'Target directory is not writable.': '目标目录不可写。',
    'Fusion requires at least 2 sources. Did you forget to uncheck fusion?':
        '文件合并至少需要 2 个来源。你是不是忘记取消勾选文件合并了？',
}

_BACKEND_WARNING_PREFIXES_ZH = (
    ('Failed to extract images from PDF file. ', '从 PDF 提取图片失败。'),
)

_FIELD_LABELS_ZH = {
    'Series': '系列',
    'Volume': '卷',
    'Number': '编号',
    'Writer': '编剧',
    'Penciller': '铅笔稿',
    'Inker': '墨线',
    'Colorist': '上色',
    'Title': '标题',
}

_MAIN_WINDOW_TEXTS_ZH = {
    'editorButton': '元数据编辑器',
    'kofiButton': '在 Ko-fi 上支持我',
    'wikiButton': 'Wiki',
    'preserveMarginLabel': '保留边距 %',
    'croppingPowerLabel': '裁剪强度：',
    'hLabel': '自定义高度：',
    'wLabel': '自定义宽度：',
    'convertButton': '转换',
    'clearButton': '清空列表',
    'fileButton': '添加输入文件',
    'directoryButton': '添加输入文件夹',
    'chunkSizeLabel': '分块大小 MB：',
    'chunkSizeWarnLabel': '大于默认值可能会影响旧设备性能。',
    'rotateFirstBox': '先旋转',
    'outputSplit': '输出分卷',
    'pdfWidthBox': 'PDF 按宽度渲染',
    'borderBox': '黑/白边距',
    'deleteBox': '删除输入',
    'spreadShiftBox': '跨页偏移',
    'maximizeStrips': '1x4 转 2x2 长条',
    'webtoonBox': '条漫模式',
    'noRotateBox': '不旋转',
    'mangaBox': '右到左（漫画）',
    'noQuantizeBox': '禁用量化',
    'jpegQualityBox': '自定义 JPEG 质量',
    'colorBox': '彩色模式',
    'disableProcessingBox': '禁用处理',
    'defaultOutputFolderBox': '输出文件夹',
    'metadataTitleBox': '元数据标题',
    'autocontrastBox': '自动对比度',
    'pdfExtractBox': 'PDF 旧版提取',
    'upscaleBox': '拉伸/放大',
    'chunkSizeCheckBox': '分块大小',
    'qualityBox': '分镜视图 4/2/HQ',
    'mozJpegBox': 'JPEG/PNG/mozJpeg',
    'eraseRainbowBox': '彩虹纹消除',
    'fileFusionBox': '文件合并',
    'coverFillBox': '封面填充',
    'rotateRightBox': '向右旋转',
    'gammaBox': '自定义伽马',
    'autoLevelBox': '极致黑点',
    'interPanelCropBox': '分镜间裁切',
    'rotateBox': '跨页拆分',
    'croppingBox': '裁剪模式',
    'pngLegacyBox': 'PNG 兼容模式',
    'forcePngRgbBox': '强制 PNG RGB',
    'gammaLabel': '伽马：自动',
    'jpegQualityLabel': 'JPEG 质量：',
}

_MAIN_WINDOW_TOOLTIPS_ZH = {
    'editorButton': '按住 Shift 点击可直接编辑目录。',
    'preserveMarginLabel': '计算裁剪边界后，按百分比保留一部分边距。',
    'hLabel': '目标设备的分辨率高度。',
    'widthBox': '目标设备的分辨率宽度。',
    'wLabel': '目标设备的分辨率宽度。',
    'heightBox': '目标设备的分辨率高度。',
    'convertButton': '按住 Shift 点击可为当前列表选择输出目录。',
    'deviceBox': '目标设备。',
    'fileButton': '将 CBR、CBZ、CB7 或 PDF 文件加入队列。',
    'directoryButton': '将包含 JPG、PNG 或 GIF 的文件夹加入队列。文件夹里的 CBR/CBZ/CB7 不会被处理。',
    'formatBox': '输出格式。',
    'jobList': '双击来源项可在元数据编辑器中打开。',
    'chunkSizeWidget': '分块大小高于默认值时，尤其在旧设备上，可能带来性能或续航问题。',
    'rotateFirstBox': '跨页拆分为半选时：未勾选表示旋转页放在拆分页后面；勾选表示放在前面。',
    'outputSplit': '未勾选为自动拆分；勾选后每个子目录都会被视为单独一卷。',
    'pdfWidthBox': '矢量 PDF 按设备宽度而不是高度渲染，适合裁掉上下边缘后铺满屏幕。',
    'borderBox': '未勾选为自动检测；半选保留白边；勾选填充黑边。',
    'deleteBox': '删除输入文件或目录，此操作无法恢复。',
    'spreadShiftBox': '在横屏模式下将第一页移到对侧，以便双页跨页对齐。',
    'maximizeStrips': '将 1x4 长条分镜改成 2x2，以提高屏幕利用率。',
    'webtoonBox': '启用韩漫/条漫的专用解析模式。',
    'noRotateBox': '在跨页拆分选项中不旋转双页跨页。',
    'mangaBox': '启用从右到左的阅读顺序。',
    'noQuantizeBox': '不将 PNG 图像量化到 16 色。文件会更大，但可保留 256 色。',
    'jpegQualityBox': '设置 JPEG 质量，范围 0 到 95。数值越大体积越大、质量越高。',
    'colorBox': '禁用灰度转换。',
    'disableProcessingBox': '不处理图片，忽略设备配置和处理选项。',
    'defaultOutputFolderBox': '未勾选输出到源文件旁边；半选输出到同级新文件夹；勾选输出到自定义目录。',
    'defaultOutputFolderButton': '选择默认输出目录。',
    'metadataTitleBox': '控制是否使用 ComicInfo.xml 或其他内嵌元数据中的标题。',
    'autocontrastBox': '设置自动对比度应用范围，或完全关闭。',
    'pdfExtractBox': '使用 KCC 8 及更早版本的 PDF 图片提取方式，适合异常 PDF。',
    'upscaleBox': '控制小于设备分辨率的图像是否拉伸或放大。',
    'chunkSizeCheckBox': '未勾选时按默认大小拆分；勾选后按“分块大小 MB”中的值拆分。',
    'qualityBox': '设置分镜视图模式：4 分镜、2 分镜或高质量 4 分镜。',
    'mozJpegBox': '在 JPEG、强制 PNG、mozJpeg 之间切换。',
    'titleEdit': '默认标题。',
    'eraseRainbowBox': '通过抑制干扰频率减轻彩色电子墨水屏上的彩虹纹。',
    'fileFusionBox': '将所有选中文件合并为一个文件，适合把章节合成整卷。',
    'coverFillBox': '先按比例居中裁切，再把封面铺满设备分辨率。',
    'rotateRightBox': '将双页跨页按与默认相反的方向旋转。',
    'gammaBox': '设置自定义伽马值。1.0 为默认，低于 1.0 更亮，高于 1.0 更暗。',
    'autoLevelBox': '将黑点映射得更激进，适合文字较黑但画面偏灰的页面。',
    'interPanelCropBox': '可裁掉分镜之间的空白横线，或同时裁掉横线与竖线。',
    'rotateBox': '设置双页跨页是拆分、拆分并旋转，还是仅旋转。',
    'authorEdit': '默认作者为 KCC。',
    'croppingBox': '设置裁剪模式：禁用、仅边距、边距加页码。',
    'pngLegacyBox': '使用兼容性更高的 8 位 PNG，而不是 4 位 PNG。',
    'forcePngRgbBox': '强制全彩图像使用无损 PNG 保存，会明显增大文件体积。',
}

_MAIN_WINDOW_PLACEHOLDERS_ZH = {
    'titleEdit': '默认标题',
    'authorEdit': '默认作者',
}

_EDITOR_TEXTS_ZH = {
    'label_1': '系列：',
    'label_2': '卷：',
    'label_3': '编号：',
    'label_4': '编剧：',
    'label_5': '铅笔稿：',
    'label_6': '墨线：',
    'label_7': '上色：',
    'label_8': '标题：',
    'okButton': '保存',
    'cancelButton': '取消',
}


@lru_cache(maxsize=1)
def is_chinese_ui():
    override = os.environ.get('KCC_UI_LANGUAGE', '').strip().lower()
    if override:
        return override.startswith('zh')
    return QLocale.system().name().lower().startswith('zh')


def tr(text):
    if not is_chinese_ui():
        return text
    return _TRANSLATIONS_ZH.get(text, text)


def trf(text, **kwargs):
    return tr(text).format(**kwargs)


def translate_backend_message(text):
    if not is_chinese_ui():
        return text
    if text in _BACKEND_WARNING_TRANSLATIONS_ZH:
        return _BACKEND_WARNING_TRANSLATIONS_ZH[text]
    for prefix, translation in _BACKEND_WARNING_PREFIXES_ZH:
        if text.startswith(prefix):
            return translation + text[len(prefix):]
    return text


def profile_label(name):
    return tr(name)


def format_label(name):
    return tr(name)


def field_label(name):
    if not is_chinese_ui():
        return name
    return _FIELD_LABELS_ZH.get(name, name)


def localize_main_window(window, ui):
    if not is_chinese_ui():
        return
    window.setWindowTitle(tr('Kindle Comic Converter'))
    for attr, value in _MAIN_WINDOW_TEXTS_ZH.items():
        getattr(ui, attr).setText(value)
    for attr, value in _MAIN_WINDOW_TOOLTIPS_ZH.items():
        getattr(ui, attr).setToolTip(value)
    for attr, value in _MAIN_WINDOW_PLACEHOLDERS_ZH.items():
        getattr(ui, attr).setPlaceholderText(value)


def localize_metadata_editor(dialog, ui):
    if not is_chinese_ui():
        return
    dialog.setWindowTitle('元数据编辑器')
    for attr, value in _EDITOR_TEXTS_ZH.items():
        getattr(ui, attr).setText(value)
