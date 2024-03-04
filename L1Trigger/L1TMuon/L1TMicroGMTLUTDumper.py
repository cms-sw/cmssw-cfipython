import FWCore.ParameterSet.Config as cms

def L1TMicroGMTLUTDumper(**kwargs):
  mod = cms.EDAnalyzer('L1TMicroGMTLUTDumper',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
