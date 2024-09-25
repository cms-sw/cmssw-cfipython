import FWCore.ParameterSet.Config as cms

def FakeTrackProducerFromCandidate(*args, **kwargs):
  mod = cms.EDProducer('FakeTrackProducerFromCandidate',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
