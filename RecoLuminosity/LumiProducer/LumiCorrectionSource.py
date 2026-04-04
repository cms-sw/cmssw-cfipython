import FWCore.ParameterSet.Config as cms

def LumiCorrectionSource(*args, **kwargs):
  mod = cms.ESSource('LumiCorrectionSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
