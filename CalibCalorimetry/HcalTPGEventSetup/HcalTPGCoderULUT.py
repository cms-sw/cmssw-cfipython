import FWCore.ParameterSet.Config as cms

def HcalTPGCoderULUT(**kwargs):
  mod = cms.ESProducer('HcalTPGCoderULUT',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
