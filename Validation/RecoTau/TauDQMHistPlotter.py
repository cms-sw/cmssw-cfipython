import FWCore.ParameterSet.Config as cms

def TauDQMHistPlotter(*args, **kwargs):
  mod = cms.EDAnalyzer('TauDQMHistPlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
