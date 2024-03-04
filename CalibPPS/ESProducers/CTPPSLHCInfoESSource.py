import FWCore.ParameterSet.Config as cms

def CTPPSLHCInfoESSource(**kwargs):
  mod = cms.ESSource('CTPPSLHCInfoESSource',
    label = cms.string(''),
    validityRange = cms.EventRange('0:18446744073709551615-0:18446744073709551615'),
    beamEnergy = cms.double(0),
    betaStar = cms.double(0),
    xangle = cms.double(0),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
