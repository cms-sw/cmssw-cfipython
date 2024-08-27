import FWCore.ParameterSet.Config as cms

def RawToText(**kwargs):
  mod = cms.EDAnalyzer('RawToText',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
