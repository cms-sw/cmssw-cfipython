import FWCore.ParameterSet.Config as cms

def EcalDigiToRaw(**kwargs):
  mod = cms.EDProducer('EcalDigiToRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
