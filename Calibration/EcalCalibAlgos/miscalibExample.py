import FWCore.ParameterSet.Config as cms

def miscalibExample(**kwargs):
  mod = cms.EDAnalyzer('miscalibExample',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
