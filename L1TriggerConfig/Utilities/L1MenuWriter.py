import FWCore.ParameterSet.Config as cms

def L1MenuWriter(**kwargs):
  mod = cms.EDAnalyzer('L1MenuWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
