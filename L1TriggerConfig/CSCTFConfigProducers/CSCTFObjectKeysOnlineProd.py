import FWCore.ParameterSet.Config as cms

def CSCTFObjectKeysOnlineProd(**kwargs):
  mod = cms.ESProducer('CSCTFObjectKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
