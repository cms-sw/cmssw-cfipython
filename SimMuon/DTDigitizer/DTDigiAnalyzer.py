import FWCore.ParameterSet.Config as cms

def DTDigiAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DTDigiAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
