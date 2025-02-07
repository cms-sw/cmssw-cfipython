import FWCore.ParameterSet.Config as cms

def MinBias(*args, **kwargs):
  mod = cms.EDAnalyzer('MinBias',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
