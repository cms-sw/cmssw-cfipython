import FWCore.ParameterSet.Config as cms

def PFTrackProducerFromL1Tracks(**kwargs):
  mod = cms.EDProducer('PFTrackProducerFromL1Tracks',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
