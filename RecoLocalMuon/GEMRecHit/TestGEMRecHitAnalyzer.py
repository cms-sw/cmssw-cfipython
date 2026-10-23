import FWCore.ParameterSet.Config as cms

def TestGEMRecHitAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestGEMRecHitAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
