# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:37:11 2020

@author: Rapha
"""

import OpenGL.GL as gl

class ModelRenderer():
    
    TRIANGLES = 1
    LINES = 2
    LINE_LOOP = 3
    
    def __init__(self, vertex_position, vertex_color=[], primitive=TRIANGLES):
        
        # triangle position and color
        self.__vertexPosition = vertex_position
        self.__vertexColor = vertex_color
        self.__primitive = primitive
        
        self.__positionVBO = 0
        self.__colorVBO = 0
        self.__VAO = 0
        
        if(len(self.__vertexPosition) > 0):
            self.__createBuffer();
        
    def __createBuffer(self):
        
        self.__VAO = gl.glGenVertexArrays(1)
        self.__positionVBO = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.__positionVBO)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, self.__vertexPosition.nbytes, self.__vertexPosition, gl.GL_STATIC_DRAW)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
        
        if(len(self.__vertexColor) > 0):
            self.__colorVBO = gl.glGenBuffers(1)
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.__colorVBO)
            gl.glBufferData(gl.GL_ARRAY_BUFFER, self.__vertexColor.nbytes, self.__vertexColor, gl.GL_STATIC_DRAW)
            gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
            
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
        
    def render(self):
        
        if(self.__VAO > 0):
            gl.glBindVertexArray(self.__VAO)

            if(self.__primitive == ModelRenderer.TRIANGLES):
                gl.glDrawArrays(gl.GL_TRIANGLES, 0, self.__vertexPosition.size // 4)
                
            elif(self.__primitive == ModelRenderer.LINES):
                gl.glDrawArrays(gl.GL_LINES, 0, self.__vertexPosition.size // 4)
            
            elif(self.__primitive == ModelRenderer.LINE_LOOP):
                gl.glDrawArrays(gl.GL_LINE_LOOP, 0, self.__vertexPosition.size // 4)

            gl.glBindVertexArray(0)