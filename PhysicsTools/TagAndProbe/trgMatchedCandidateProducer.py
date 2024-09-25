import FWCore.ParameterSet.Config as cms

def trgMatchedCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('trgMatchedCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
