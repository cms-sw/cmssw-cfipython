import FWCore.ParameterSet.Config as cms

def DoodadESSource(**kwargs):
  mod = cms.ESSource('DoodadESSource',
    appendToDataLabel = cms.optional.string,
    test2 = cms.optional.untracked.string,
    test = cms.untracked.bool(False)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
