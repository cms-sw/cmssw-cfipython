import FWCore.ParameterSet.Config as cms

def L1GctPrintLuts(**kwargs):
  mod = cms.EDAnalyzer('L1GctPrintLuts',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
