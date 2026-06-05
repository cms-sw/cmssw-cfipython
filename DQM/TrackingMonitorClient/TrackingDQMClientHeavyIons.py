import FWCore.ParameterSet.Config as cms

def TrackingDQMClientHeavyIons(*args, **kwargs):
  mod = cms.EDProducer('TrackingDQMClientHeavyIons',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
