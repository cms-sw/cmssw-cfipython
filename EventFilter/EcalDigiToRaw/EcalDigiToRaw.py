import FWCore.ParameterSet.Config as cms

def EcalDigiToRaw(*args, **kwargs):
  mod = cms.EDProducer('EcalDigiToRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
