import FWCore.ParameterSet.Config as cms

def CaloMiscalibTools(*args, **kwargs):
  mod = cms.ESSource('CaloMiscalibTools',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
