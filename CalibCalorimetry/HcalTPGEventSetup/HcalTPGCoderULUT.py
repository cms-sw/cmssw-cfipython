import FWCore.ParameterSet.Config as cms

def HcalTPGCoderULUT(*args, **kwargs):
  mod = cms.ESProducer('HcalTPGCoderULUT',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
