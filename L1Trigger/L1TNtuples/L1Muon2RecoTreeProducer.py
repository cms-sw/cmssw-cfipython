import FWCore.ParameterSet.Config as cms

def L1Muon2RecoTreeProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('L1Muon2RecoTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
