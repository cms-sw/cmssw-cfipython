import FWCore.ParameterSet.Config as cms

def PoolDBESSource(**kwargs):
  mod = cms.ESSource('PoolDBESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
