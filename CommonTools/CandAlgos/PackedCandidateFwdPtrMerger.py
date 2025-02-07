import FWCore.ParameterSet.Config as cms

def PackedCandidateFwdPtrMerger(*args, **kwargs):
  mod = cms.EDProducer('PackedCandidateFwdPtrMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
