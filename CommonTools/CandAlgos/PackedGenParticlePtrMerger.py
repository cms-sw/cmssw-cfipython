import FWCore.ParameterSet.Config as cms

def PackedGenParticlePtrMerger(**kwargs):
  mod = cms.EDProducer('PackedGenParticlePtrMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
