import FWCore.ParameterSet.Config as cms

def SiStripLatencyFakeESSource(*args, **kwargs):
  mod = cms.ESSource('SiStripLatencyFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
