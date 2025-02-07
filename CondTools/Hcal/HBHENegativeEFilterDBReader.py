import FWCore.ParameterSet.Config as cms

def HBHENegativeEFilterDBReader(*args, **kwargs):
  mod = cms.EDAnalyzer('HBHENegativeEFilterDBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
