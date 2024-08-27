import FWCore.ParameterSet.Config as cms

def PPSStraightTrackAligner(**kwargs):
  mod = cms.EDAnalyzer('PPSStraightTrackAligner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
