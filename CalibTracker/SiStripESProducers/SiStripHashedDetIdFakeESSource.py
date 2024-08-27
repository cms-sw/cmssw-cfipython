import FWCore.ParameterSet.Config as cms

def SiStripHashedDetIdFakeESSource(**kwargs):
  mod = cms.ESProducer('SiStripHashedDetIdFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
