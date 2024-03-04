import FWCore.ParameterSet.Config as cms

def PATPFParticleProducer(**kwargs):
  mod = cms.EDProducer('PATPFParticleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
