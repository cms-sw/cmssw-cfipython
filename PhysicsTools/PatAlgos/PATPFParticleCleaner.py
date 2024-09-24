import FWCore.ParameterSet.Config as cms

def PATPFParticleCleaner(*args, **kwargs):
  mod = cms.EDProducer('PATPFParticleCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
