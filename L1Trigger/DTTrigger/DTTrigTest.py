import FWCore.ParameterSet.Config as cms

def DTTrigTest(*args, **kwargs):
  mod = cms.EDAnalyzer('DTTrigTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
