import FWCore.ParameterSet.Config as cms

from .TrackerDigiGeometryESModule import TrackerDigiGeometryESModule

trackerGeometryDB = TrackerDigiGeometryESModule(
  appendToDataLabel = '',
  fromDDD = False,
  applyAlignment = True,
  alignmentsLabel = ''
)
