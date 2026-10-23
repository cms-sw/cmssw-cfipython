import FWCore.ParameterSet.Config as cms

def TtSemiLepSignalSelMVAFileSource(*args, **kwargs):
  mod = cms.ESSource('TtSemiLepSignalSelMVAFileSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
