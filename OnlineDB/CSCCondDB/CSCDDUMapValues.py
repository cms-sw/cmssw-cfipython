import FWCore.ParameterSet.Config as cms

def CSCDDUMapValues(*args, **kwargs):
  mod = cms.ESSource('CSCDDUMapValues',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
