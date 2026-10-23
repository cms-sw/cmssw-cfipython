import FWCore.ParameterSet.Config as cms

def DTTTrigCorrection(*args, **kwargs):
  mod = cms.EDAnalyzer('DTTTrigCorrection',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
