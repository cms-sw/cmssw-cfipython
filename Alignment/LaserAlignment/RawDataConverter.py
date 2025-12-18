import FWCore.ParameterSet.Config as cms

def RawDataConverter(*args, **kwargs):
  mod = cms.EDAnalyzer('RawDataConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
