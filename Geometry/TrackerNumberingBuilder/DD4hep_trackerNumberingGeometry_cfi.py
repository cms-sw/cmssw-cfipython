import FWCore.ParameterSet.Config as cms

from .TrackerGeometricDetESModule import TrackerGeometricDetESModule

DD4hep_trackerNumberingGeometry = TrackerGeometricDetESModule(
  fromDDD = False,
  fromDD4hep = True,
  appendToDataLabel = ''
)
