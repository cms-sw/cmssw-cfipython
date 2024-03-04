import FWCore.ParameterSet.Config as cms

def trklet_ProducerAS(**kwargs):
  mod = cms.EDProducer('trklet::ProducerAS',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
