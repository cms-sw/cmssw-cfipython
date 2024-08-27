import FWCore.ParameterSet.Config as cms

def LaserDQM(**kwargs):
  mod = cms.EDAnalyzer('LaserDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
