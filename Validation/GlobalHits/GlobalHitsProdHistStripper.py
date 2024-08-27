import FWCore.ParameterSet.Config as cms

def GlobalHitsProdHistStripper(**kwargs):
  mod = cms.EDAnalyzer('GlobalHitsProdHistStripper',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
