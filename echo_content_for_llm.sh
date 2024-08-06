#!/bin/bash

directory="."
script_name=$(basename "$0")
output_file="claude_context.txt"

print_tree() {
    echo "Directory Structure:"
    find "$directory" -not -path '*/\.*' -not -path '*/venv/*' -not -path '*/output/*' -not -path '*/results/*' | sort | sed -e "s/[^-][^\/]*\// |/g" -e "s/|\([^ ]\)/|-\1/"
    echo "---"
}

print_file_contents() {
    local file=$1
    if [ -f "$file" ] && [ "$(basename "$file")" != "$script_name" ] && [ "$(basename "$file")" != "$output_file" ]; then
        echo "Contents of $file:"
        echo "FILE START: $file"
        cat "$file"
        echo "FILE END: $file"
        echo "---"
    fi
}

if [ -d "$directory" ]; then
    print_tree

    find "$directory" \( -name "*.py" -o -name "*.yaml" -o -name "*.tf" -o -name ".env.example" -o -name "*.sh" -o -name "Dockerfile" -o -name "*.md" -o -name ".gitignore" -o -name "requirements.txt" -o -name "CONTRIBUTING.md" -o -name "docs/*.md" -o -name "*.json" \) -type f | sort | while read -r file; do
        print_file_contents "$file"
    done
else
    echo "Directory $directory does not exist."
fi