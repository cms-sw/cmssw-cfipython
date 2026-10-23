import FWCore.ParameterSet.Config as cms

def HBHEDarkeningAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HBHEDarkeningAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
