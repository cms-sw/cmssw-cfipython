import FWCore.ParameterSet.Config as cms

def RawToText(*args, **kwargs):
  mod = cms.EDAnalyzer('RawToText',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
