import FWCore.ParameterSet.Config as cms

def PatTauAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PatTauAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
