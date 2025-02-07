import FWCore.ParameterSet.Config as cms

def RunLumiESSource(*args, **kwargs):
  mod = cms.ESSource('RunLumiESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
