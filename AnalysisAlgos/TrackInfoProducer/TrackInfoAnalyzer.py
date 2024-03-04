import FWCore.ParameterSet.Config as cms

def TrackInfoAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TrackInfoAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
