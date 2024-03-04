import FWCore.ParameterSet.Config as cms

def TestMix(**kwargs):
  mod = cms.EDAnalyzer('TestMix',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
