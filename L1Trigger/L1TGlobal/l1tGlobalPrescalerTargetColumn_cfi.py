import FWCore.ParameterSet.Config as cms

l1tGlobalPrescalerTargetColumn = cms.EDFilter('L1TGlobalPrescaler',
  l1tResults = cms.InputTag('gtStage2Digis'),
  mode = cms.string('applyColumnRatios'),
  l1tPrescaleColumn = cms.uint32(0)
)
