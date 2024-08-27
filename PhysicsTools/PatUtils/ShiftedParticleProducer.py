import FWCore.ParameterSet.Config as cms

def ShiftedParticleProducer(**kwargs):
  mod = cms.EDProducer('ShiftedParticleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
