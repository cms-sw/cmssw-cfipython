import FWCore.ParameterSet.Config as cms

def ShiftedParticleProducer(*args, **kwargs):
  mod = cms.EDProducer('ShiftedParticleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
