import FWCore.ParameterSet.Config as cms

def TtSemiLepSignalSelMVAFileSource(**kwargs):
  mod = cms.ESSource('TtSemiLepSignalSelMVAFileSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
