import FWCore.ParameterSet.Config as cms

def AnyNumbersToValueMaps(**kwargs):
  mod = cms.EDProducer('AnyNumbersToValueMaps',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
