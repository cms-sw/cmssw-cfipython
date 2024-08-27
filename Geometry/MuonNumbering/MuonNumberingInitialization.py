import FWCore.ParameterSet.Config as cms

def MuonNumberingInitialization(**kwargs):
  mod = cms.ESProducer('MuonNumberingInitialization',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
