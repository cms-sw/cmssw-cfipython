import FWCore.ParameterSet.Config as cms

def PATPFParticleCleaner(**kwargs):
  mod = cms.EDProducer('PATPFParticleCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
