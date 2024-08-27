import FWCore.ParameterSet.Config as cms

def JetPlusTrackProducerAA(**kwargs):
  mod = cms.EDProducer('JetPlusTrackProducerAA',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
