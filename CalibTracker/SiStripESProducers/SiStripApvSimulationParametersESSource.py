import FWCore.ParameterSet.Config as cms

def SiStripApvSimulationParametersESSource(**kwargs):
  mod = cms.ESSource('SiStripApvSimulationParametersESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
