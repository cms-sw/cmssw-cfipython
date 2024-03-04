import FWCore.ParameterSet.Config as cms

def MLexampleModule_1(**kwargs):
  mod = cms.EDAnalyzer('MLexampleModule_1',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
