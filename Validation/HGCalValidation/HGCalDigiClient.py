import FWCore.ParameterSet.Config as cms

def HGCalDigiClient(**kwargs):
  mod = cms.EDProducer('HGCalDigiClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
