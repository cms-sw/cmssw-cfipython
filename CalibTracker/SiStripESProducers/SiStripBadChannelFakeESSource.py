import FWCore.ParameterSet.Config as cms

def SiStripBadChannelFakeESSource(*args, **kwargs):
  mod = cms.ESSource('SiStripBadChannelFakeESSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
