import FWCore.ParameterSet.Config as cms

def TestCaloAlignmentEP(**kwargs):
  mod = cms.ESProducer('TestCaloAlignmentEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
