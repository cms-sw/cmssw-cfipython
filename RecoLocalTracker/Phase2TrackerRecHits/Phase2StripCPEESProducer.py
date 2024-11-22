import FWCore.ParameterSet.Config as cms

def Phase2StripCPEESProducer(*args, **kwargs):
  mod = cms.ESProducer('Phase2StripCPEESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
