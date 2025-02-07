import FWCore.ParameterSet.Config as cms

def GenParticleMatchMerger(*args, **kwargs):
  mod = cms.EDProducer('GenParticleMatchMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
