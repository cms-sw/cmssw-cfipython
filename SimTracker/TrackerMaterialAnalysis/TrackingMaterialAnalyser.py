import FWCore.ParameterSet.Config as cms

def TrackingMaterialAnalyser(**kwargs):
  mod = cms.EDAnalyzer('TrackingMaterialAnalyser',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
