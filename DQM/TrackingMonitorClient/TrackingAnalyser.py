import FWCore.ParameterSet.Config as cms

def TrackingAnalyser(**kwargs):
  mod = cms.EDProducer('TrackingAnalyser',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
