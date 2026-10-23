import FWCore.ParameterSet.Config as cms

def DoodadESSource(*args, **kwargs):
  mod = cms.ESSource('DoodadESSource',
    appendToDataLabel = cms.optional.string,
    test2 = cms.optional.untracked.string,
    test = cms.untracked.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
