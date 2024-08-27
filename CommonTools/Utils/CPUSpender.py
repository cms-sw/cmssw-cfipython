import FWCore.ParameterSet.Config as cms

def CPUSpender(**kwargs):
  mod = cms.EDAnalyzer('CPUSpender',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
