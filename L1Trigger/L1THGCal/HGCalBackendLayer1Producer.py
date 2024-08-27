import FWCore.ParameterSet.Config as cms

def HGCalBackendLayer1Producer(**kwargs):
  mod = cms.EDProducer('HGCalBackendLayer1Producer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
