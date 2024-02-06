import FWCore.ParameterSet.Config as cms

l1TTauComparisonResultFilter = cms.EDFilter('L1TTauComparisonResultFilter',
  objComparisonColl = cms.InputTag('objComparisonColl'),
  maxBxRangeDiff = cms.int32(-1),
  maxExcess = cms.int32(-1),
  maxSize = cms.int32(-1),
  invert = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
