import FWCore.ParameterSet.Config as cms

def PackedCandidateFwdPtrMerger(**kwargs):
  mod = cms.EDProducer('PackedCandidateFwdPtrMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
