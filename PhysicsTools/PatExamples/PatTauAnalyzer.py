import FWCore.ParameterSet.Config as cms

def PatTauAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PatTauAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
