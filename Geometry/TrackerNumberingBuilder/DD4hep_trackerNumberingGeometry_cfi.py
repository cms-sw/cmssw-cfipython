import FWCore.ParameterSet.Config as cms

from .TrackerGeometricDetESModule import TrackerGeometricDetESModule

DD4hep_trackerNumberingGeometry = TrackerGeometricDetESModule(

  fromDD4hep = True
)
