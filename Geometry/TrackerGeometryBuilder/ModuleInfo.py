import FWCore.ParameterSet.Config as cms

def ModuleInfo(**kwargs):
  mod = cms.EDAnalyzer('ModuleInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
