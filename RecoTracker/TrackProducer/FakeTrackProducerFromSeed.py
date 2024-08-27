import FWCore.ParameterSet.Config as cms

def FakeTrackProducerFromSeed(**kwargs):
  mod = cms.EDProducer('FakeTrackProducerFromSeed',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
