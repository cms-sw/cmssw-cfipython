import FWCore.ParameterSet.Config as cms

def TrackingCertificationInfo(**kwargs):
  mod = cms.EDProducer('TrackingCertificationInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
