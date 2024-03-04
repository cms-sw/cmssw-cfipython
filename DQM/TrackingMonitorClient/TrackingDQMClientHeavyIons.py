import FWCore.ParameterSet.Config as cms

def TrackingDQMClientHeavyIons(**kwargs):
  mod = cms.EDProducer('TrackingDQMClientHeavyIons',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
