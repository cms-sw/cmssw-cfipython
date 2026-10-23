import FWCore.ParameterSet.Config as cms

def PFMatchedCandidateRefExtractor(*args, **kwargs):
  mod = cms.EDProducer('PFMatchedCandidateRefExtractor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
