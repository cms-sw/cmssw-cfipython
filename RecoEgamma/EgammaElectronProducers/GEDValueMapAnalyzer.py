import FWCore.ParameterSet.Config as cms

def GEDValueMapAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('GEDValueMapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
