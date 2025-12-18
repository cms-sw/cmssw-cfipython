import FWCore.ParameterSet.Config as cms

def IntProductESSource(*args, **kwargs):
  mod = cms.ESSource('IntProductESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
