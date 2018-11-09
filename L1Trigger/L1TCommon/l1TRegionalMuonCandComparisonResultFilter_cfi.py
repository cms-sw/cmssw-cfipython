import FWCore.ParameterSet.Config as cms

l1TRegionalMuonCandComparisonResultFilter = cms.EDFilter('L1TRegionalMuonCandComparisonResultFilter',
  objComparisonColl = cms.InputTag('objComparisonColl'),
  maxBxRangeDiff = cms.int32(-1),
  maxExcess = cms.int32(-1),
  maxSize = cms.int32(-1),
  invert = cms.bool(False)
)