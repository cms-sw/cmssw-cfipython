import FWCore.ParameterSet.Config as cms

def FakeTrackProducerFromCandidate(**kwargs):
  mod = cms.EDProducer('FakeTrackProducerFromCandidate',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
