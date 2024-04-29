from Lib import __lib_topaz__ as topaz
from Lib import __lib_kafka__ as kafka 
from Lib import __lib_archeron__ as archeron
from Lib import __lib_stelle__ as stelle
import unreal, importlib
import time

importlib.reload(topaz)
importlib.reload(kafka)
importlib.reload(archeron)
importlib.reload(stelle)

# Path: downsize/downsize_disk_size_of_textures.py

list_tex :list[unreal.Texture2D] = archeron.get_all_textures_in_folder('/Game/CitySample/Textures')

def remap_uepath_to_filepath(uepath: str) -> str: #언리얼 패스 -> 파일 패스로 변환
    '''
    ## Description: Remap the Unreal Engine path to the file path
    '''
    projectPath = unreal.Paths.project_dir()
    #print(projectPath)
    filepath = uepath.replace('/Game/', projectPath + 'Content/')
    name = filepath.rsplit('.', 1)[0]
    name = name + '.uasset'
    return name

def export_texture ( texture_asset : unreal.Texture2D, target_file_path : str, exporter) : #textureExporter
    exportTask = unreal.AssetExportTask()
    
    exportTask.automated = True
    exportTask.filename = target_file_path
    exportTask.object = texture_asset
    exportTask.prompt = False
    exportTask.exporter = exporter

    exporter.run_asset_export_task(exportTask)
    return True


#텍스처 선택
selectedAssets = unreal.EditorUtilityLibrary.get_selected_assets()
ImagePathList = []

desired_size = 2048

#선택된 텍스처 익스포트
for asset in selectedAssets:
    tex_size_x = asset.blueprint_get_size_x()
    is_virtual_texture = False
    #asset.get_editor_property('virtual_texture_streaming')
    
    # 조건
    needs_export = tex_size_x > desired_size
    
    if needs_export :
        # 변경 목록 전체숫자 체크 용도
        ImagePathList.append(asset)

        tex_path = asset.get_path_name()
        import_info = asset.get_editor_property('asset_import_data')
        source_file = import_info.get_first_filename()
        
        #이미지 저장할 드라이브 경로
        target_drive = 'E:/wip/'
        source_drive = unreal.Paths.project_dir().split('/')[0] + '/'

        new_tex_path = remap_uepath_to_filepath(tex_path).replace(source_drive, target_drive)
        file_path: str
        hasPNG = source_file.lower().find('.png')
        hasTGA = source_file.lower().find('.tga')
        hasJPG = source_file.lower().find('.jpg')

        if hasPNG != -1:
            print('This is PNG')
            file_path = new_tex_path.replace('.uasset','.png')
            exporter = unreal.TextureExporterPNG()
        elif hasTGA != -1:
            print('This is TGA')
            exporter = unreal.TextureExporterTGA()
            file_path = new_tex_path.replace('.uasset','.tga')
        elif hasJPG != -1:
            print('This is TGA')
            exporter = unreal.TextureExporterJPEG()
            file_path = new_tex_path.replace('.uasset','.tga')
        else:
            # to-do > rgba채널 사용하는 텍스처면 tga로 아니면 png로 익스포트하게하기
            print('This is PNG')
            exporter = unreal.TextureExporterTGA()
            file_path = new_tex_path.replace('.uasset','.tga')
        export_texture(asset, file_path, exporter)
        time.sleep(2)
print(' ************** ', len(ImagePathList),' ************** ')