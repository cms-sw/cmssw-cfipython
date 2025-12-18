import FWCore.ParameterSet.Config as cms

def DumpBtagTable(*args, **kwargs):
  mod = cms.EDAnalyzer('DumpBtagTable',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
