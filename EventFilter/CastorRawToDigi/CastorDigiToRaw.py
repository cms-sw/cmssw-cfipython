import FWCore.ParameterSet.Config as cms

def CastorDigiToRaw(**kwargs):
  mod = cms.EDProducer('CastorDigiToRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
