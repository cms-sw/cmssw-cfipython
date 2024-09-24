import FWCore.ParameterSet.Config as cms

def PATCompositeCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('PATCompositeCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
