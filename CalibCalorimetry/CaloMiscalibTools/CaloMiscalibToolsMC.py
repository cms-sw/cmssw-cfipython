import FWCore.ParameterSet.Config as cms

def CaloMiscalibToolsMC(**kwargs):
  mod = cms.ESSource('CaloMiscalibToolsMC',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
