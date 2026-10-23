import FWCore.ParameterSet.Config as cms

def TrackCategoriesAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackCategoriesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
