import FWCore.ParameterSet.Config as cms

def TrackCategoriesAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TrackCategoriesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
