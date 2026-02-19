import FWCore.ParameterSet.Config as cms

from .MTDGeometricTimingDetESModule import MTDGeometricTimingDetESModule

mtdNumberingGeometry = MTDGeometricTimingDetESModule(

  fromDDD = True
)
