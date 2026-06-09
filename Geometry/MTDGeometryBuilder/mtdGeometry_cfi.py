import FWCore.ParameterSet.Config as cms

from .MTDDigiGeometryESModule import MTDDigiGeometryESModule

mtdGeometry = MTDDigiGeometryESModule(

  fromDDD = True
)
