import FWCore.ParameterSet.Config as cms

def L1Muon2RecoTreeProducer(**kwargs):
  mod = cms.EDAnalyzer('L1Muon2RecoTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
