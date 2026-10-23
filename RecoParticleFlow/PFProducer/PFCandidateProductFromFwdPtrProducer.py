import FWCore.ParameterSet.Config as cms

def PFCandidateProductFromFwdPtrProducer(*args, **kwargs):
  mod = cms.EDProducer('PFCandidateProductFromFwdPtrProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
