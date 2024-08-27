import FWCore.ParameterSet.Config as cms

def printEvent(**kwargs):
  mod = cms.EDAnalyzer('printEvent',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
