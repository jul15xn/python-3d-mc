#version 330 core

layout (location = 0) in vec3 in_position;
layout (location = 1) in vec3 in_color;

uniform mat4 m_proj;
uniform mat4 m_view;
uniform mat4 m_model;

out vec3 color;
out vec2 uv;

const vec2 uv_coords[4] = vec2[4](
    vec2(0,0), vec2(0,1),
    vec2(1,0), vec2(1,1)
);

const int uv_indices[12] = int[12](
    1, 0, 2, 1, 2, 3, // tex coords indices for vertices of an even face
    3, 0, 2, 3, 1, 0  // odd face 
);

void main() {
    int uv_index = gl_VertexID % 6 + (face_id & 1) * 6;
    uv = uv_coords[uv_indices[uv_index]];
    color = in_color;
    gl_Position = m_proj * m_view * m_model * vec4(in_position, 1.0);
}