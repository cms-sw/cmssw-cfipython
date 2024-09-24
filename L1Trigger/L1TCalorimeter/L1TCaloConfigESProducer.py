import FWCore.ParameterSet.Config as cms

def L1TCaloConfigESProducer(*args, **kwargs):
  mod = cms.ESProducer('L1TCaloConfigESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod