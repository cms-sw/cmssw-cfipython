import FWCore.ParameterSet.Config as cms

def L1GTDigiToRaw(**kwargs):
  mod = cms.EDProducer('L1GTDigiToRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod