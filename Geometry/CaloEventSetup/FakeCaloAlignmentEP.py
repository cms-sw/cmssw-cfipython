import FWCore.ParameterSet.Config as cms

def FakeCaloAlignmentEP(**kwargs):
  mod = cms.ESProducer('FakeCaloAlignmentEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
