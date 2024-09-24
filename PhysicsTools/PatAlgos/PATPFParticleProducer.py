import FWCore.ParameterSet.Config as cms

def PATPFParticleProducer(*args, **kwargs):
  mod = cms.EDProducer('PATPFParticleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
