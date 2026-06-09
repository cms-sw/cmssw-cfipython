import FWCore.ParameterSet.Config as cms

def SiStripConnectivity(*args, **kwargs):
  mod = cms.ESProducer('SiStripConnectivity',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
