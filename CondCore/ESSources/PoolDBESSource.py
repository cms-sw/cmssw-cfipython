import FWCore.ParameterSet.Config as cms

def PoolDBESSource(*args, **kwargs):
  mod = cms.ESSource('PoolDBESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
