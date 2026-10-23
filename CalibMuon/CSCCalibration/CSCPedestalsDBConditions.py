import FWCore.ParameterSet.Config as cms

def CSCPedestalsDBConditions(*args, **kwargs):
  mod = cms.ESSource('CSCPedestalsDBConditions',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
