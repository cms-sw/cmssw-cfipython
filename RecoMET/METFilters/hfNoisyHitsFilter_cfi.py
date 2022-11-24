import FWCore.ParameterSet.Config as cms

hfNoisyHitsFilter = cms.EDFilter('HFNoisyHitsFilter',
  hfrechits = cms.InputTag('reducedHcalRecHits', 'hfreco'),
  rechitPtThreshold = cms.double(20),
  listOfNoises = cms.vstring(
    'HFLongShort',
    'HFS8S1Ratio',
    'HFPET',
    'HFSignalAsymmetry'
  ),
  taggingMode = cms.bool(False),
  debug = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
