import FWCore.ParameterSet.Config as cms

def HGCalBackendStage1Producer(**kwargs):
  mod = cms.EDProducer('HGCalBackendStage1Producer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
