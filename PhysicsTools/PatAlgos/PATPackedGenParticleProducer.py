import FWCore.ParameterSet.Config as cms

def PATPackedGenParticleProducer(**kwargs):
  mod = cms.EDProducer('PATPackedGenParticleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod