import FWCore.ParameterSet.Config as cms

def JetComparison(*args, **kwargs):
  mod = cms.EDAnalyzer('JetComparison',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
