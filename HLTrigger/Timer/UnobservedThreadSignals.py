import FWCore.ParameterSet.Config as cms

def UnobservedThreadSignals(*args, **kwargs):
  mod = cms.Service('UnobservedThreadSignals',
    moduleLabel = cms.required.untracked.string
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
