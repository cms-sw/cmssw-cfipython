import FWCore.ParameterSet.Config as cms

def ModuleInfo_Phase2(*args, **kwargs):
  mod = cms.EDAnalyzer('ModuleInfo_Phase2',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
