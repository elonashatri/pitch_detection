import os
import xml.etree.ElementTree as ET

# Define source and target directories
source_dir = "/Users/eshatri/Desktop/split_by_complexity/monophonic/xml_by_page"
target_dir = "/Users/eshatri/Desktop/split_by_complexity/monophonic_only_pos"

# Iterate over all XML files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith('.xml'):
        # Parse the XML
        tree = ET.parse(os.path.join(source_dir, filename))
        root = tree.getroot()

        # Create a new root for the output XML
        output_root = ET.Element(root.tag)

        # Iterate over all 'Node' elements
        for node in root.iter('Node'):
            class_name = node.find('ClassName')
            
            # If ClassName starts with "note"
            if class_name is not None and class_name.text.startswith('note'):
                # Find the DataItem with key="line_pos"
                line_pos = node.find("./Data/DataItem[@key='line_pos']")
                
                # If found, replace ClassName with line_pos
                if line_pos is not None:
                    class_name.text = line_pos.text
                    
                    # Append the node to the output root
                    output_root.append(node)

        # Write the modified XML to a new file in the target directory
        output_tree = ET.ElementTree(output_root)
        output_tree.write(os.path.join(target_dir, filename))
