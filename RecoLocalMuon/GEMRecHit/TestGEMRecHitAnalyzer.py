import FWCore.ParameterSet.Config as cms

def TestGEMRecHitAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestGEMRecHitAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
