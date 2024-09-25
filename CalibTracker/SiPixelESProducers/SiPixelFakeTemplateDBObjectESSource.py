import FWCore.ParameterSet.Config as cms

def SiPixelFakeTemplateDBObjectESSource(*args, **kwargs):
  mod = cms.ESSource('SiPixelFakeTemplateDBObjectESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
