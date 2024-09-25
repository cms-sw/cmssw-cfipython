import FWCore.ParameterSet.Config as cms

def HFNoisyHitsFilter(*args, **kwargs):
  mod = cms.EDFilter('HFNoisyHitsFilter',
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
