import unreal 
from Lib import __lib_topaz__ as topaz

import importlib

importlib.reload(topaz)

selectedAssets = unreal.EditorUtilityLibrary.get_selected_assets()
# print(selectedAssets[0])
staticMeshsInBP = topaz.get_component_by_class(selectedAssets[0], unreal.StaticMeshComponent)

directoryPath = selectedAssets[0].get_path_name()
part = directoryPath.split('/')
staticMeshesDirectory = '/'.join(part[:6]) + '/06StaticMeshes' 
print(staticMeshesDirectory)  

for staticMesh in staticMeshsInBP:
    # print(staticMesh.static_mesh.get_name())
    arr = staticMesh.static_mesh.get_path_name().split('/')
    length = len(arr)
    staticMeshFilesName = arr[length-1]
    targetPath = staticMeshesDirectory + '/' + staticMeshFilesName
    print(targetPath)
    sourcePath = staticMesh.static_mesh.get_path_name()
    unreal.EditorAssetLibrary.RenameAsset(sourcePath, targetPath)

    # unreal.EditorAssetLibrary.RenameAsset(staticMesh.static_mesh, targetPath)