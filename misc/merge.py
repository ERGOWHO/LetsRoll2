import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


train1_data = load_json('_annotations.coco.json')
train2_data = load_json('1_annotations.coco.json')


max_image_id_train1 = max(img['id'] for img in train1_data['images'])

id_mapping = {}
new_image_id = max_image_id_train1
for image in train2_data['images']:
    new_image_id += 1  # 更新 image_id
    id_mapping[image['id']] = new_image_id  # 记录旧 image_id 到新 image_id 的映射
    image['id'] = new_image_id  # 实际更新 image_id

for annotation in train2_data['annotations']:
    original_image_id = annotation['image_id']
    # 使用映射表更新 annotation 的 image_id
    annotation['image_id'] = id_mapping[original_image_id]


merged_images = train1_data['images'] + train2_data['images']
merged_annotations = train1_data['annotations'] + train2_data['annotations']


merged_data = {
    "images": merged_images,
    "annotations": merged_annotations,
    "categories": train1_data['categories']  # 假设 categories 不需要更新
}

merged_file_path = 'train_annotations.coco.json'
with open(merged_file_path, 'w', encoding='utf-8') as file:
    json.dump(merged_data, file, ensure_ascii=False, indent=4)

print(f"Merged file saved to {merged_file_path}")
