# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:37:11 2020

@author: Rapha
"""

import OpenGL.GL as gl

class ModelRenderer():
    
    POINTS = 0
    LINES = 1
    LINE_LOOP = 2
    LINE_STRIP = 3
    TRIANGLES = 4
    TRIANGLE_STRIP = 5
    TRIANGLE_FAN = 6
    
    def __init__(self, vertex_position, vertex_indices=[], vertex_color=[], vertex_normal=[], primitive=TRIANGLES):
        
        gl_primitives = [gl.GL_POINTS,
                         gl.GL_LINES, gl.GL_LINE_LOOP, gl.GL_LINE_STRIP,
                         gl.GL_TRIANGLES, gl.GL_TRIANGLE_STRIP, gl.GL_TRIANGLE_FAN]
        
        self.__vertexPosition = vertex_position
        self.__vertexIndices = vertex_indices
        self.__vertexColor = vertex_color
        self.__vertexNormal = vertex_normal
        
        if(primitive >= 0 and primitive <= 6):
            self.__primitive = gl_primitives[primitive]
        else:
            print('ModelRenderer: primitiva inválida. Mudando para a primitiva TRIANGLES.')
            self.__primitive = gl.GL_TRIANGLES
        
        self.__positionVBO = 0
        self.__colorVBO = 0
        self.__normalVBO = 0
        self.__EBO = 0
        self.__VAO = 0
        
        if(len(self.__vertexPosition) > 0):
            self.__createBuffer();
        
    def __createBuffer(self):
        
        self.__VAO = gl.glGenVertexArrays(1)
        self.__positionVBO = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.__positionVBO)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, self.__vertexPosition.nbytes, self.__vertexPosition, gl.GL_STATIC_DRAW)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
        
        if(len(self.__vertexIndices) > 0):
            gl.glBindVertexArray(self.__VAO)
            self.__EBO = gl.glGenBuffers(1)
            gl.glBindBuffer(gl.GL_ELEMENT_ARRAY_BUFFER, self.__EBO)
            gl.glBufferData(gl.GL_ELEMENT_ARRAY_BUFFER, self.__vertexIndices.nbytes, self.__vertexIndices, gl.GL_STATIC_DRAW)
            gl.glBindVertexArray(0);
            
        if(len(self.__vertexColor) > 0):
            self.__colorVBO = gl.glGenBuffers(1)
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.__colorVBO)
            gl.glBufferData(gl.GL_ARRAY_BUFFER, self.__vertexColor.nbytes, self.__vertexColor, gl.GL_STATIC_DRAW)
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
            
        if(len(self.__vertexNormal) > 0):
            self.__normalVBO = gl.glGenBuffers(1)
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.__normalVBO)
            gl.glBufferData(gl.GL_ARRAY_BUFFER, self.__vertexNormal.nbytes, self.__vertexNormal, gl.GL_STATIC_DRAW)
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
        
    def setVertexPositionLoc(self, position_loc):
        
        if(self.__positionVBO > 0):
            gl.glBindVertexArray(self.__VAO)
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.__positionVBO)
            gl.glEnableVertexAttribArray(position_loc)
            gl.glVertexAttribPointer(position_loc, 4, gl.GL_FLOAT, gl.GL_FALSE, 0, None)
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
            gl.glBindVertexArray(0)
        
    def setVertexColorLoc(self, color_loc):
        
        if(self.__colorVBO > 0):
            gl.glBindVertexArray(self.__VAO)
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.__colorVBO)
            gl.glEnableVertexAttribArray(color_loc)
            gl.glVertexAttribPointer(color_loc, 4, gl.GL_FLOAT, gl.GL_FALSE, 0, None)
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
            gl.glBindVertexArray(0)
            
    def setVertexNormalLoc(self, normal_loc):
        
        if(self.__normalVBO > 0):
            gl.glBindVertexArray(self.__VAO)
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.__normalVBO)
            gl.glEnableVertexAttribArray(normal_loc)
            gl.glVertexAttribPointer(normal_loc, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, None)
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
            gl.glBindVertexArray(0)
    
    def updateVertexPositions(self, vertex_position):
        
        if(self.__positionVBO > 0):
            self.__vertexPosition = vertex_position
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.__positionVBO)
            gl.glBufferData(gl.GL_ARRAY_BUFFER, self.__vertexPosition.nbytes, self.__vertexPosition, gl.GL_STATIC_DRAW)
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
            
    def updateVertexColors(self, vertex_color):
        
        if(self.__colorVBO > 0):
            self.__vertexColor = vertex_color
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.__colorVBO)
            gl.glBufferData(gl.GL_ARRAY_BUFFER, self.__vertexColor.nbytes, self.__vertexColor, gl.GL_STATIC_DRAW)
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
    
    def updateVertexNormals(self, vertex_normals):
        
        if(self.__normalVBO > 0):
            self.__vertexNormal = vertex_normals
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.__normalVBO)
            gl.glBufferData(gl.GL_ARRAY_BUFFER, self.__vertexNormal.nbytes, self.__vertexNormal, gl.GL_STATIC_DRAW)
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
            
    def render(self):
        
        if(self.__VAO > 0):
            gl.glBindVertexArray(self.__VAO)

            if(self.__EBO == 0):
                gl.glDrawArrays(self.__primitive, 0, self.__vertexPosition.size // 4)
            else:
                gl.glDrawElements(self.__primitive, self.__vertexIndices.size, gl.GL_UNSIGNED_INT, None)

            gl.glBindVertexArray(0)
    
    def renderWireframe(self):
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE);
        
        self.render()
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL);