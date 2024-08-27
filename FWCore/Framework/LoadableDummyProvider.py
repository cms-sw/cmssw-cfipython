import FWCore.ParameterSet.Config as cms

def LoadableDummyProvider(**kwargs):
  mod = cms.ESProducer('LoadableDummyProvider',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
