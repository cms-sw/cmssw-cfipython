import FWCore.ParameterSet.Config as cms

def trgMatchedChargedCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('trgMatchedChargedCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
