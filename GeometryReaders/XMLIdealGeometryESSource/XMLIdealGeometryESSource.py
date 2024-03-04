import FWCore.ParameterSet.Config as cms

def XMLIdealGeometryESSource(**kwargs):
  mod = cms.ESSource('XMLIdealGeometryESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
