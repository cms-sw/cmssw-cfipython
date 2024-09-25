import FWCore.ParameterSet.Config as cms

def SiStripApvSimulationParametersESSource(*args, **kwargs):
  mod = cms.ESSource('SiStripApvSimulationParametersESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
