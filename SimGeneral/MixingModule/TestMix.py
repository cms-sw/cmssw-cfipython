import FWCore.ParameterSet.Config as cms

def TestMix(*args, **kwargs):
  mod = cms.EDAnalyzer('TestMix',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
