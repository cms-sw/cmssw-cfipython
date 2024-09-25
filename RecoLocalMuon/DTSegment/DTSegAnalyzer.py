import FWCore.ParameterSet.Config as cms

def DTSegAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DTSegAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
