import FWCore.ParameterSet.Config as cms

def trklet_ProducerDR(*args, **kwargs):
  mod = cms.EDProducer('trklet::ProducerDR',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
