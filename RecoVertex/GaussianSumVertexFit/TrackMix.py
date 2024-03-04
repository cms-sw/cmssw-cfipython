import FWCore.ParameterSet.Config as cms

def TrackMix(**kwargs):
  mod = cms.EDAnalyzer('TrackMix',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
