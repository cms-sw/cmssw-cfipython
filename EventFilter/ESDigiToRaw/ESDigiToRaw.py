import FWCore.ParameterSet.Config as cms

def ESDigiToRaw(**kwargs):
  mod = cms.EDProducer('ESDigiToRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
