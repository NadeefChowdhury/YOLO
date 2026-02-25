# yolo label format: class x_center y_center width height 
import glob

def change_labels_index(labels_path, new_class_mappings):
    """Change the index of labels to match the new class mappings for yolo"""
    for label_file in glob.glob(labels_path + "/*.txt"):
        with open(label_file, "r") as f:
            lines = f.readlines()
        with open(label_file, "w") as f:
            for line in lines:
                class_index = int(line.split(" ")[0])
                new_class_index = new_class_mappings[class_index]
                f.write(str(new_class_index) + " " + line.split(" ", 1)[1])


"""
the keys are original class index and the values are the new class index that you want to map to.
Below is the example for RTTS detection dataset to nRain Dataset
"""

#NOTE: Please set the paths to your own paths
labels_path = 'D:/Python codes/YOLO Cat/cat/labels'
new_class_mappings = {
   25:0
}
change_labels_index(labels_path, new_class_mappings)