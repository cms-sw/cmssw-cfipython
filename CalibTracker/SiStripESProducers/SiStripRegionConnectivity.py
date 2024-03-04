import FWCore.ParameterSet.Config as cms

def SiStripRegionConnectivity(**kwargs):
  mod = cms.ESProducer('SiStripRegionConnectivity',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
