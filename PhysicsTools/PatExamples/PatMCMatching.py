import FWCore.ParameterSet.Config as cms

def PatMCMatching(**kwargs):
  mod = cms.EDAnalyzer('PatMCMatching',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
