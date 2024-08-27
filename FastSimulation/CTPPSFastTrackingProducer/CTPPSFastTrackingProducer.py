import FWCore.ParameterSet.Config as cms

def CTPPSFastTrackingProducer(**kwargs):
  mod = cms.EDProducer('CTPPSFastTrackingProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
