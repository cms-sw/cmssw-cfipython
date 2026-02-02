import FWCore.ParameterSet.Config as cms

from .TrackerGeometricDetESModule import TrackerGeometricDetESModule

trackerNumberingGeometryDB = TrackerGeometricDetESModule(
  fromDDD = False,
  fromDD4hep = False,
  appendToDataLabel = ''
)
