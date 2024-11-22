import FWCore.ParameterSet.Config as cms

def DD4hep_ListIds(*args, **kwargs):
  mod = cms.EDAnalyzer('DD4hep_ListIds',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
