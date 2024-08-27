import FWCore.ParameterSet.Config as cms

def TrackReader(**kwargs):
  mod = cms.EDAnalyzer('TrackReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
