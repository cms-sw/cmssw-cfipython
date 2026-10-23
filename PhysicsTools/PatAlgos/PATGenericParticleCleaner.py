import FWCore.ParameterSet.Config as cms

def PATGenericParticleCleaner(*args, **kwargs):
  mod = cms.EDProducer('PATGenericParticleCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
