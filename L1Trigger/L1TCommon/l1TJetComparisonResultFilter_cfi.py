import FWCore.ParameterSet.Config as cms

l1TJetComparisonResultFilter = cms.EDFilter('L1TJetComparisonResultFilter',
  objComparisonColl = cms.InputTag('objComparisonColl'),
  maxBxRangeDiff = cms.int32(-1),
  maxExcess = cms.int32(-1),
  maxSize = cms.int32(-1),
  invert = cms.bool(False)
)
