import FWCore.ParameterSet.Config as cms

def TrackValidator(**kwargs):
  mod = cms.EDAnalyzer('TrackValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
