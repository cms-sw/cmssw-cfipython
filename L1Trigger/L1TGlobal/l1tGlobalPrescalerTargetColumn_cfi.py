import FWCore.ParameterSet.Config as cms

from .L1TGlobalPrescaler import L1TGlobalPrescaler

l1tGlobalPrescalerTargetColumn = L1TGlobalPrescaler(
  l1tResults = ('gtStage2Digis'),
  mode = 'applyColumnRatios',
  l1tPrescaleColumn = cms.uint32(0)
)
