import FWCore.ParameterSet.Config as cms

def CSCTFObjectKeysOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('CSCTFObjectKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
