import FWCore.ParameterSet.Config as cms

def HGCalBackendLayer2Producer(*args, **kwargs):
  mod = cms.EDProducer('HGCalBackendLayer2Producer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
