import FWCore.ParameterSet.Config as cms

def FWLiteESSource(*args, **kwargs):
  mod = cms.ESSource('FWLiteESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
