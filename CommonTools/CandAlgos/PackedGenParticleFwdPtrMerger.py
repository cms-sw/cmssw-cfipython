import FWCore.ParameterSet.Config as cms

def PackedGenParticleFwdPtrMerger(**kwargs):
  mod = cms.EDProducer('PackedGenParticleFwdPtrMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
