import FWCore.ParameterSet.Config as cms

def DataCardFileWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('DataCardFileWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
