import FWCore.ParameterSet.Config as cms

def GlobalHitsProdHistStripper(*args, **kwargs):
  mod = cms.EDAnalyzer('GlobalHitsProdHistStripper',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
