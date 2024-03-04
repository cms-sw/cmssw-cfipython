import FWCore.ParameterSet.Config as cms

def MVAComputerESSource(**kwargs):
  mod = cms.ESSource('MVAComputerESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
