import FWCore.ParameterSet.Config as cms

def FWLiteESSource(**kwargs):
  mod = cms.ESSource('FWLiteESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
