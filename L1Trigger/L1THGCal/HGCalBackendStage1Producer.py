import FWCore.ParameterSet.Config as cms

def HGCalBackendStage1Producer(*args, **kwargs):
  mod = cms.EDProducer('HGCalBackendStage1Producer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
