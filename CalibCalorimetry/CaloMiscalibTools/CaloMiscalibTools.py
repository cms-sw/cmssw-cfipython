import FWCore.ParameterSet.Config as cms

def CaloMiscalibTools(**kwargs):
  mod = cms.ESSource('CaloMiscalibTools',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
