import FWCore.ParameterSet.Config as cms

def CSCFakePedestalsConditions(**kwargs):
  mod = cms.ESSource('CSCFakePedestalsConditions',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod