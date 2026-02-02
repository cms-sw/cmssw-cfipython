import FWCore.ParameterSet.Config as cms

from .MTDDigiGeometryESModule import MTDDigiGeometryESModule

mtdGeometryDB = MTDDigiGeometryESModule(
  appendToDataLabel = '',
  fromDDD = False,
  applyAlignment = True,
  alignmentsLabel = ''
)
