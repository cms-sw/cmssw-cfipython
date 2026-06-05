import FWCore.ParameterSet.Config as cms

def CTPPSPixelDAQMappingESSourceXML(*args, **kwargs):
  mod = cms.ESSource('CTPPSPixelDAQMappingESSourceXML',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
