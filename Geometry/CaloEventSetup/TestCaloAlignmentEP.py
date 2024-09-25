import FWCore.ParameterSet.Config as cms

def TestCaloAlignmentEP(*args, **kwargs):
  mod = cms.ESProducer('TestCaloAlignmentEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
