import FWCore.ParameterSet.Config as cms

def trklet_ProducerKFin(*args, **kwargs):
  mod = cms.EDProducer('trklet::ProducerKFin',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
