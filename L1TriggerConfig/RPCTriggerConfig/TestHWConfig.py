import FWCore.ParameterSet.Config as cms

def TestHWConfig(**kwargs):
  mod = cms.EDAnalyzer('TestHWConfig',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
