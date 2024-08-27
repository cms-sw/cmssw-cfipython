import FWCore.ParameterSet.Config as cms

def HiSignalParticleProducer(**kwargs):
  mod = cms.EDProducer('HiSignalParticleProducer',
    src = cms.InputTag('genParticles'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
