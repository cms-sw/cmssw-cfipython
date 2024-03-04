import FWCore.ParameterSet.Config as cms

def MVADemoFileSource(**kwargs):
  mod = cms.ESSource('MVADemoFileSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
