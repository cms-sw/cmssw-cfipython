import FWCore.ParameterSet.Config as cms

def HGCalBackendLayer1Producer(*args, **kwargs):
  mod = cms.EDProducer('HGCalBackendLayer1Producer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod