import FWCore.ParameterSet.Config as cms

def ParticleFlowForChargedMETProducer(**kwargs):
  mod = cms.EDProducer('ParticleFlowForChargedMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
