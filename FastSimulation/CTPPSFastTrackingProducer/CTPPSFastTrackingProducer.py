import FWCore.ParameterSet.Config as cms

def CTPPSFastTrackingProducer(*args, **kwargs):
  mod = cms.EDProducer('CTPPSFastTrackingProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
