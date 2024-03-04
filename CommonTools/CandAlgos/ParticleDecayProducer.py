import FWCore.ParameterSet.Config as cms

def ParticleDecayProducer(**kwargs):
  mod = cms.EDProducer('ParticleDecayProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
