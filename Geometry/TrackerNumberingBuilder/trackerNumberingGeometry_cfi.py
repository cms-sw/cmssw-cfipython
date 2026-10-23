import FWCore.ParameterSet.Config as cms

from .TrackerGeometricDetESModule import TrackerGeometricDetESModule

trackerNumberingGeometry = TrackerGeometricDetESModule(

  fromDDD = True
)
