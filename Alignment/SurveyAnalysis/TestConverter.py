import FWCore.ParameterSet.Config as cms

def TestConverter(**kwargs):
  mod = cms.EDAnalyzer('TestConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
