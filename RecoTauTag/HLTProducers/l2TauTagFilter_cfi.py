import FWCore.ParameterSet.Config as cms

l2TauTagFilter = cms.EDFilter('L2TauTagFilter',
  saveTags = cms.bool(True),
  nExpected = cms.int32(2),
  L1TauSrc = cms.InputTag(''),
  L2Outcomes = cms.InputTag(''),
  DiscrWP = cms.double(0.1227),
  mightGet = cms.optional.untracked.vstring
)
