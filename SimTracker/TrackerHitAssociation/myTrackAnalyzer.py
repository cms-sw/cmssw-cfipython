import FWCore.ParameterSet.Config as cms

def myTrackAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('myTrackAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
