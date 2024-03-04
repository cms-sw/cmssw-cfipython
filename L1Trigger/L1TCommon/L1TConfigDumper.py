import FWCore.ParameterSet.Config as cms

def L1TConfigDumper(**kwargs):
  mod = cms.EDAnalyzer('L1TConfigDumper',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
