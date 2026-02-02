import FWCore.ParameterSet.Config as cms

from .TrackerDigiGeometryESModule import TrackerDigiGeometryESModule

trackerGeometry = TrackerDigiGeometryESModule(
  appendToDataLabel = '',
  fromDDD = True,
  applyAlignment = True,
  alignmentsLabel = ''
)
