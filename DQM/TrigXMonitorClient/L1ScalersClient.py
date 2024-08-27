import FWCore.ParameterSet.Config as cms

def L1ScalersClient(**kwargs):
  mod = cms.EDAnalyzer('L1ScalersClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
