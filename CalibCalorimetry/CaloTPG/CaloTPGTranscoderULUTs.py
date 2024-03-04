import FWCore.ParameterSet.Config as cms

def CaloTPGTranscoderULUTs(**kwargs):
  mod = cms.ESProducer('CaloTPGTranscoderULUTs',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
