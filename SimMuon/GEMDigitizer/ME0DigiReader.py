import FWCore.ParameterSet.Config as cms

def ME0DigiReader(**kwargs):
  mod = cms.EDAnalyzer('ME0DigiReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
