import FWCore.ParameterSet.Config as cms

def CSCTFConfigOnlineProd(**kwargs):
  mod = cms.ESProducer('CSCTFConfigOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
