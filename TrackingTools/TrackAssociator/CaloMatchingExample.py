import FWCore.ParameterSet.Config as cms

def CaloMatchingExample(**kwargs):
  mod = cms.EDAnalyzer('CaloMatchingExample',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
