import FWCore.ParameterSet.Config as cms

def EcalLaserCorrectionService(**kwargs):
  mod = cms.ESProducer('EcalLaserCorrectionService',
    maxExtrapolationTimeInSec = cms.uint32(0),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
