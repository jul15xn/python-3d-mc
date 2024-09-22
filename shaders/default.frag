#version 330 core

layout (location = 0) out vec4 fragColor;

in vec2 uv_0;

uniform sampler2D uv_texture_0;

void main() {
    vec3 color = texture(uv_texture_0, uv_0).rgb;
    fragColor = vec4(color, 1.0);
}