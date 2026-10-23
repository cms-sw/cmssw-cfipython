import FWCore.ParameterSet.Config as cms

def MTDCPEESProducer(*args, **kwargs):
  mod = cms.ESProducer('MTDCPEESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
