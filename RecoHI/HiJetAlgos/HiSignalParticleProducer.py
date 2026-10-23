import FWCore.ParameterSet.Config as cms

def HiSignalParticleProducer(*args, **kwargs):
  mod = cms.EDProducer('HiSignalParticleProducer',
    src = cms.InputTag('genParticles'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
