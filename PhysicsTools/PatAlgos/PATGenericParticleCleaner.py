import FWCore.ParameterSet.Config as cms

def PATGenericParticleCleaner(**kwargs):
  mod = cms.EDProducer('PATGenericParticleCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
