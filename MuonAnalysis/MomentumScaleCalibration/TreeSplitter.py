import FWCore.ParameterSet.Config as cms

def TreeSplitter(*args, **kwargs):
  mod = cms.EDAnalyzer('TreeSplitter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
