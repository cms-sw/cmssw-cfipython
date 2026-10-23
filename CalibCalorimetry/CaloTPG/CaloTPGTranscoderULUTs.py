import FWCore.ParameterSet.Config as cms

def CaloTPGTranscoderULUTs(*args, **kwargs):
  mod = cms.ESProducer('CaloTPGTranscoderULUTs',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
