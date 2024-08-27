import FWCore.ParameterSet.Config as cms

def CSCDDUMapValues(**kwargs):
  mod = cms.ESSource('CSCDDUMapValues',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
