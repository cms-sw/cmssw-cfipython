import FWCore.ParameterSet.Config as cms

def AnalyticalTrackSelector(**kwargs):
  mod = cms.EDProducer('AnalyticalTrackSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
