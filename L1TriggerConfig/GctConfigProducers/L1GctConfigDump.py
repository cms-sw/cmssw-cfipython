import FWCore.ParameterSet.Config as cms

def L1GctConfigDump(**kwargs):
  mod = cms.EDAnalyzer('L1GctConfigDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
