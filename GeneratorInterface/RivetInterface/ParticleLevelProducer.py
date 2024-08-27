import FWCore.ParameterSet.Config as cms

def ParticleLevelProducer(**kwargs):
  mod = cms.EDProducer('ParticleLevelProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
