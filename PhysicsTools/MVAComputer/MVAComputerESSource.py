import FWCore.ParameterSet.Config as cms

def MVAComputerESSource(*args, **kwargs):
  mod = cms.ESSource('MVAComputerESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
