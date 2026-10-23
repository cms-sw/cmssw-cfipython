import FWCore.ParameterSet.Config as cms

def SiStripBackPlaneCorrectionFakeESSource(*args, **kwargs):
  mod = cms.ESSource('SiStripBackPlaneCorrectionFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
