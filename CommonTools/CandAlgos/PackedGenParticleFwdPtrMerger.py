import FWCore.ParameterSet.Config as cms

def PackedGenParticleFwdPtrMerger(*args, **kwargs):
  mod = cms.EDProducer('PackedGenParticleFwdPtrMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
