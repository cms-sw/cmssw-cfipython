import FWCore.ParameterSet.Config as cms

def PFCandidateProductFromFwdPtrProducer(**kwargs):
  mod = cms.EDProducer('PFCandidateProductFromFwdPtrProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
