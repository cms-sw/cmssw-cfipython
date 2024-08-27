import FWCore.ParameterSet.Config as cms

def SiStripFedCablingFakeESSource(**kwargs):
  mod = cms.ESSource('SiStripFedCablingFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
