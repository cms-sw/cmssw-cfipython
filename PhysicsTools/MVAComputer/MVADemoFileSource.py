import FWCore.ParameterSet.Config as cms

def MVADemoFileSource(*args, **kwargs):
  mod = cms.ESSource('MVADemoFileSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
