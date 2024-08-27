import FWCore.ParameterSet.Config as cms

def TtFullHadSignalSelMVAFileSource(**kwargs):
  mod = cms.ESSource('TtFullHadSignalSelMVAFileSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
