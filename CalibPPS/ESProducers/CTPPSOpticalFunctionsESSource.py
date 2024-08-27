import FWCore.ParameterSet.Config as cms

def CTPPSOpticalFunctionsESSource(**kwargs):
  mod = cms.ESSource('CTPPSOpticalFunctionsESSource',
    label = cms.string(''),
    configuration = cms.VPSet(
    ),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
