import FWCore.ParameterSet.Config as cms

def TrackingParticleCategoriesAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TrackingParticleCategoriesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
