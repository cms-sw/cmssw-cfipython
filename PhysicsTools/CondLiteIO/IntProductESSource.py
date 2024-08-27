import FWCore.ParameterSet.Config as cms

def IntProductESSource(**kwargs):
  mod = cms.ESSource('IntProductESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
