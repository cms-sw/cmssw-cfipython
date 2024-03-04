import FWCore.ParameterSet.Config as cms

def SiStripConnectivity(**kwargs):
  mod = cms.ESProducer('SiStripConnectivity',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
