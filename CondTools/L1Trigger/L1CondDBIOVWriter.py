import FWCore.ParameterSet.Config as cms

def L1CondDBIOVWriter(**kwargs):
  mod = cms.EDAnalyzer('L1CondDBIOVWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
