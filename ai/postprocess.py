def clean_modules(modules):
    cleaned = []
    seen = set()

    for m in modules:
        module_name = m["module"].lower()

        # Merge similar modules
        if "support" in module_name or "help" in module_name:
            module_key = "Support & Help"
        elif "technical" in module_name:
            module_key = "Technical Guides"
        elif "start" in module_name or "overview" in module_name:
            module_key = "Getting Started"
        elif "publish" in module_name:
            module_key = "Publishing"
        elif "custom" in module_name or "block" in module_name:
            module_key = "Customization & Blocks"
        else:
            module_key = m["module"]

        if module_key not in seen:
            cleaned.append({
                "module": module_key,
                "Description": m["Description"] if m["Description"] else "Refer to documentation for details.",
                "Submodules": {k: v if v else "Feature related to this module."
                               for k, v in m["Submodules"].items()}
            })
            seen.add(module_key)

    return cleaned
