import FWCore.ParameterSet.Config as cms

def PATPackedCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('PATPackedCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
