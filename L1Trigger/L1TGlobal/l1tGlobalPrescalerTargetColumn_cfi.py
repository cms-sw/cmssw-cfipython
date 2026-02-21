import FWCore.ParameterSet.Config as cms

from .L1TGlobalPrescaler import L1TGlobalPrescaler

l1tGlobalPrescalerTargetColumn = L1TGlobalPrescaler(

  l1tPrescaleColumn = cms.uint32(0),
  l1tPrescales = None,
  mode = 'applyColumnRatios'
)
