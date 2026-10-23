import FWCore.ParameterSet.Config as cms

def HcalAlignmentEP(*args, **kwargs):
  mod = cms.ESProducer('HcalAlignmentEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
