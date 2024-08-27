import FWCore.ParameterSet.Config as cms

def RunLumiESSource(**kwargs):
  mod = cms.ESSource('RunLumiESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
