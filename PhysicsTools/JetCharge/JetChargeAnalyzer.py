import FWCore.ParameterSet.Config as cms

def JetChargeAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('JetChargeAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
