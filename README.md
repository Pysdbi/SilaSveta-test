# SilaSveta-test
Тестовое задание. Nuxt.js / Jquery

## Задача 1

Запрос к бэкэнду вернул объект:

```python
const data = {
    "id":2257,
    "title":"AUH reactor",
    "description":"Some description",
    "asset_files":[
        {
            "file":"assets/2257/fbx/AUH_2003_reactor_v02.fbx",
            "file_id":"f47d08ff-8887-4220-8005-a781e7188c6c",
            "file_size":18150720,
            "folder_name":"fbx",
            "grid_preview":false,
            "is_preview":false,
            "is_selected_as_preview":false,
            "is_generated_preview":false,
            "is_video_sequence_image":false,
            "is_video_main_image":false,
            "frames_count":null,
            "link":"media/assets/2257/AUH_2003_reactor_v02.fbx"
        },
        {
            "file":"assets/2257/AUH_2003_reactor_v02.c4d",
            "file_id":"df326836-3d1f-468f-9d21-f75b7c1a04ee",
            "file_size":21790398,
            "folder_name":null,
            "grid_preview":false,
            "is_preview":false,
            "is_selected_as_preview":false,
            "is_generated_preview":false,
            "is_video_sequence_image":false,
            "is_video_main_image":false,
            "frames_count":null,
            "link":"media/assets/2257/AUH_2003_reactor_v02.c4d"
        },
        {
            "file":"assets/2257/fbx/AUH_2003_GENERATOR_v06.fbx",
            "file_id":"83299502-b51e-4419-882b-2d8c08cec432",
            "file_size":42592464,
            "folder_name":"fbx",
            "grid_preview":false,
            "is_preview":false,
            "is_selected_as_preview":false,
            "is_generated_preview":false,
            "is_video_sequence_image":false,
            "is_video_main_image":false,
            "frames_count":null,
            "link":"media/assets/2257/AUH_2003_GENERATOR_v06.fbx"
        },
        {
            "file":"assets/2257/AUH_2003_GENERATOR_v06.c4d",
            "file_id":"037488c3-1677-48e5-95c7-e54ecd431c0c",
            "file_size":67900117,
            "folder_name":null,
            "grid_preview":false,
            "is_preview":false,
            "is_selected_as_preview":false,
            "is_generated_preview":false,
            "is_video_sequence_image":false,
            "is_video_main_image":false,
            "frames_count":null,
            "link":"media/assets/2257/AUH_2003_GENERATOR_v06.c4d"
        },
        {
            "file":"assets/2257/preview/reactor_preview_wireframe_1.png",
            "file_id":"2bb9cc56-ce11-4ac1-836c-e30e06e17231",
            "file_size":1177556,
            "folder_name":null,
            "grid_preview":false,
            "is_preview":true,
            "is_selected_as_preview":true,
            "is_generated_preview":false,
            "is_video_sequence_image":false,
            "is_video_main_image":false,
            "frames_count":null,
            "link":"media/assets/2257/preview/reactor_preview_wireframe_1.png"
        },
        {
            "file":"assets/2257/preview/reactor_preview_ao_2.png",
            "file_id":"60865c38-ba46-4456-b00b-afd1e2d963c1",
            "file_size":2121818,
            "folder_name":null,
            "grid_preview":false,
            "is_preview":true,
            "is_selected_as_preview":true,
            "is_generated_preview":true,
            "is_video_sequence_image":false,
            "is_video_main_image":false,
            "frames_count":null,
            "link":"media/assets/2257/preview/reactor_preview_ao_2.png"
        }
    ],
    "creation_date":"2021-07-30T11:28:51.064327Z"
}
```

Получите список объектов {file_id: file_size}, содержащий информацию о файлах, соответствующих следующим условиям:

1. Размер больше 2000000
2. Значение folder_name файла является null
3. Значение file не содержит в себе подстроку 'GENERATOR'

Полученный список должен быть отсортирован по полю file_size в порядке возрастания

## Задача 2

В компоненте Vue получите из текущего URL [http://127.0.0.1/typeId=1&assetId=16](http://127.0.0.1/typeId=1&assetId=16) значение query-параметра assetId

## Задача 3

С помощью библиотеки jQuery замените текстовое содержимое элемента с id_toChange на изображение [https://i.pinimg.com/originals/e1/92/62/e1926225f3613de044c897241e60d47e.jpg](https://i.pinimg.com/originals/e1/92/62/e1926225f3613de044c897241e60d47e.jpg) шириной 400px и разместите указанный элемент по центру body

## Результат ждем в виде ссылки на GitHub, GitLab, BitBucket или любой другой репозиторий кода.
