FRAMEWORKS = {
    "CRAFT": "Context: {context}\nRole: {role}\nAction: {action}\nFormat: {format}\nTone: {tone}",
    "RTF": "Role: {role}\nTask: {task}\nFormat: {format}",
    "RISEN": "Role: {role}\nInstructions: {instructions}\nSteps: {steps}\nEnd goal: {goal}\nNarrowing: {constraints}",
}


def render_template(name: str, **values: str) -> str:
    return FRAMEWORKS[name].format(**values)
