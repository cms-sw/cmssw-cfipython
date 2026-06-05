import FWCore.ParameterSet.Config as cms

def ParticleFlowForChargedMETProducer(*args, **kwargs):
  mod = cms.EDProducer('ParticleFlowForChargedMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
