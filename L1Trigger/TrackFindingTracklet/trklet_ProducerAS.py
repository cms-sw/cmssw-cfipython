import FWCore.ParameterSet.Config as cms

def trklet_ProducerAS(*args, **kwargs):
  mod = cms.EDProducer('trklet::ProducerAS',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
