import FWCore.ParameterSet.Config as cms

def jetMatch(*args, **kwargs):
  mod = cms.EDAnalyzer('jetMatch',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
