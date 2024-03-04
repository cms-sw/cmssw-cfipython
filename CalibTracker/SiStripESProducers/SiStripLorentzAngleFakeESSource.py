import FWCore.ParameterSet.Config as cms

def SiStripLorentzAngleFakeESSource(**kwargs):
  mod = cms.ESSource('SiStripLorentzAngleFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
