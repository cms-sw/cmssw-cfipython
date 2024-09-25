import FWCore.ParameterSet.Config as cms

def RPCSectorAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCSectorAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
