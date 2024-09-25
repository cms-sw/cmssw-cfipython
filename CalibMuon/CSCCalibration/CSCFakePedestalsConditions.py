import FWCore.ParameterSet.Config as cms

def CSCFakePedestalsConditions(*args, **kwargs):
  mod = cms.ESSource('CSCFakePedestalsConditions',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
