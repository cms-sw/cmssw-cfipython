import FWCore.ParameterSet.Config as cms

def trgMatchChargedCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('trgMatchChargedCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
