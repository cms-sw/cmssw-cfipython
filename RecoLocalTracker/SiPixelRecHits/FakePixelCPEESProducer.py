import FWCore.ParameterSet.Config as cms

def FakePixelCPEESProducer(*args, **kwargs):
  mod = cms.ESProducer('FakePixelCPEESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
