import FWCore.ParameterSet.Config as cms

def EventSetupIntProductAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EventSetupIntProductAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
