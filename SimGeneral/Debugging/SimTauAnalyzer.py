import FWCore.ParameterSet.Config as cms

def SimTauAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('SimTauAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
