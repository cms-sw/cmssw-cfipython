import FWCore.ParameterSet.Config as cms

def DTuROSDigiToRaw(**kwargs):
  mod = cms.EDProducer('DTuROSDigiToRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
