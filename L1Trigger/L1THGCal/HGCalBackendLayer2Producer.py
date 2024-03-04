import FWCore.ParameterSet.Config as cms

def HGCalBackendLayer2Producer(**kwargs):
  mod = cms.EDProducer('HGCalBackendLayer2Producer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
