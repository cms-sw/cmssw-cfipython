import FWCore.ParameterSet.Config as cms

def SiStripRegionConnectivity(*args, **kwargs):
  mod = cms.ESProducer('SiStripRegionConnectivity',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
