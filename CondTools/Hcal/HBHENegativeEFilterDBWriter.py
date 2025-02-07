import FWCore.ParameterSet.Config as cms

def HBHENegativeEFilterDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('HBHENegativeEFilterDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
