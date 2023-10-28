import FWCore.ParameterSet.Config as cms

tauTagFilter = cms.EDFilter('TauTagFilter',
  saveTags = cms.bool(True),
  nExpected = cms.int32(2),
  taus = cms.InputTag(''),
  tauTags = cms.InputTag(''),
  tauPtCorr = cms.InputTag(''),
  seeds = cms.InputTag(''),
  seedTypes = cms.vint32(
    -100,
    -99,
    84,
    85
  ),
  selection = cms.string('0'),
  minPt = cms.double(20),
  maxEta = cms.double(2.5),
  usePtCorr = cms.bool(False),
  matchWithSeeds = cms.bool(False),
  matchingdR = cms.double(0.5),
  mightGet = cms.optional.untracked.vstring
)
