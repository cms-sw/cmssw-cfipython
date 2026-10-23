import FWCore.ParameterSet.Config as cms

def trklet_ProducerKF(*args, **kwargs):
  mod = cms.EDProducer('trklet::ProducerKF',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
