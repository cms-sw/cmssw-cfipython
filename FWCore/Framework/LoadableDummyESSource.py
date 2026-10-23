import FWCore.ParameterSet.Config as cms

def LoadableDummyESSource(*args, **kwargs):
  mod = cms.ESSource('LoadableDummyESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
