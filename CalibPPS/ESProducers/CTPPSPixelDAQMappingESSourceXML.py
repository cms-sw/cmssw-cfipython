import FWCore.ParameterSet.Config as cms

def CTPPSPixelDAQMappingESSourceXML(**kwargs):
  mod = cms.ESSource('CTPPSPixelDAQMappingESSourceXML',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
