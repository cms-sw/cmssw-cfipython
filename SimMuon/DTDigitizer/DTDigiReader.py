import FWCore.ParameterSet.Config as cms

def DTDigiReader(*args, **kwargs):
  mod = cms.EDAnalyzer('DTDigiReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
