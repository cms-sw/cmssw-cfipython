import FWCore.ParameterSet.Config as cms

def CSCPedestalsDBConditions(**kwargs):
  mod = cms.ESSource('CSCPedestalsDBConditions',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
