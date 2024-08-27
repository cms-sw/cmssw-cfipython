import FWCore.ParameterSet.Config as cms

def HBHENegativeEFilterDBWriter(**kwargs):
  mod = cms.EDAnalyzer('HBHENegativeEFilterDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
