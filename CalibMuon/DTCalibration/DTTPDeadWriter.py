import FWCore.ParameterSet.Config as cms

def DTTPDeadWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('DTTPDeadWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
