import FWCore.ParameterSet.Config as cms

def SiStripLatencyFakeESSource(**kwargs):
  mod = cms.ESSource('SiStripLatencyFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
