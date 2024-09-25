import FWCore.ParameterSet.Config as cms

def SiStripHashedDetIdFakeESSource(*args, **kwargs):
  mod = cms.ESProducer('SiStripHashedDetIdFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
