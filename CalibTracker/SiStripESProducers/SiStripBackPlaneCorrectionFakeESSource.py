import FWCore.ParameterSet.Config as cms

def SiStripBackPlaneCorrectionFakeESSource(**kwargs):
  mod = cms.ESSource('SiStripBackPlaneCorrectionFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
