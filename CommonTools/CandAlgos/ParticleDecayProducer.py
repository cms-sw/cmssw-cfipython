import FWCore.ParameterSet.Config as cms

def ParticleDecayProducer(*args, **kwargs):
  mod = cms.EDProducer('ParticleDecayProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
