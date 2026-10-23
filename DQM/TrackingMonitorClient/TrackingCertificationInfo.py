import FWCore.ParameterSet.Config as cms

def TrackingCertificationInfo(*args, **kwargs):
  mod = cms.EDProducer('TrackingCertificationInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
