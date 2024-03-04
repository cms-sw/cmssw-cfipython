import FWCore.ParameterSet.Config as cms

def PFMatchedCandidateRefExtractor(**kwargs):
  mod = cms.EDProducer('PFMatchedCandidateRefExtractor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
