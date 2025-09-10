import FWCore.ParameterSet.Config as cms

def PFTrackProducerFromL1Tracks(*args, **kwargs):
  mod = cms.EDProducer('PFTrackProducerFromL1Tracks',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
