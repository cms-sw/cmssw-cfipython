import FWCore.ParameterSet.Config as cms

def L1GtPsbSetupConfigOnlineProd(**kwargs):
  mod = cms.ESProducer('L1GtPsbSetupConfigOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod