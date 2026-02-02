import FWCore.ParameterSet.Config as cms

from .MTDDigiGeometryESModule import MTDDigiGeometryESModule

mtdGeometry = MTDDigiGeometryESModule(
  appendToDataLabel = '',
  fromDDD = True,
  applyAlignment = True,
  alignmentsLabel = ''
)
