import FWCore.ParameterSet.Config as cms

def CTPPSOpticalFunctionsESSource(*args, **kwargs):
  mod = cms.ESSource('CTPPSOpticalFunctionsESSource',
    label = cms.string(''),
    configuration = cms.VPSet(
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
