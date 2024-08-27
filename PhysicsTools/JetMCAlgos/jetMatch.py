import FWCore.ParameterSet.Config as cms

def jetMatch(**kwargs):
  mod = cms.EDAnalyzer('jetMatch',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
