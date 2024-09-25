import FWCore.ParameterSet.Config as cms

def CaloMiscalibToolsMC(*args, **kwargs):
  mod = cms.ESSource('CaloMiscalibToolsMC',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
