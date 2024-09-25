import FWCore.ParameterSet.Config as cms

def L1TMicroGMTLUTDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TMicroGMTLUTDumper',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
