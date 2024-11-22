import FWCore.ParameterSet.Config as cms

def DSVAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DSVAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
