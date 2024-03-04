import FWCore.ParameterSet.Config as cms

def MergedGenParticleProducer(**kwargs):
  mod = cms.EDProducer('MergedGenParticleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
