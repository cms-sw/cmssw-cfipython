import FWCore.ParameterSet.Config as cms

def StripCPEESProducer(*args, **kwargs):
  mod = cms.ESProducer('StripCPEESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
