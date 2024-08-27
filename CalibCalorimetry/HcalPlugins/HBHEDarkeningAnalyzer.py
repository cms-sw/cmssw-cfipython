import FWCore.ParameterSet.Config as cms

def HBHEDarkeningAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HBHEDarkeningAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
