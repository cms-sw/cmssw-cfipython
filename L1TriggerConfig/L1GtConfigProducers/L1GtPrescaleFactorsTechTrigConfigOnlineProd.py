import FWCore.ParameterSet.Config as cms

def L1GtPrescaleFactorsTechTrigConfigOnlineProd(**kwargs):
  mod = cms.ESProducer('L1GtPrescaleFactorsTechTrigConfigOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
