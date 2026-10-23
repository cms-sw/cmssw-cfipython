import FWCore.ParameterSet.Config as cms

def TtFullHadSignalSelMVAFileSource(*args, **kwargs):
  mod = cms.ESSource('TtFullHadSignalSelMVAFileSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
