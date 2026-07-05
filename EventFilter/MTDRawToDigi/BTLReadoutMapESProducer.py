import FWCore.ParameterSet.Config as cms

def BTLReadoutMapESProducer(*args, **kwargs):
  mod = cms.ESProducer('BTLReadoutMapESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
