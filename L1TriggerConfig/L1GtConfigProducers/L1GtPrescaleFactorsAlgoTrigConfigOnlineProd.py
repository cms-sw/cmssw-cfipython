import FWCore.ParameterSet.Config as cms

def L1GtPrescaleFactorsAlgoTrigConfigOnlineProd(**kwargs):
  mod = cms.ESProducer('L1GtPrescaleFactorsAlgoTrigConfigOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
