import FWCore.ParameterSet.Config as cms

def PFCandidateFromFwdPtrProducer(*args, **kwargs):
  mod = cms.EDProducer('PFCandidateFromFwdPtrProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
