import FWCore.ParameterSet.Config as cms

def trgMatchCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('trgMatchCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
