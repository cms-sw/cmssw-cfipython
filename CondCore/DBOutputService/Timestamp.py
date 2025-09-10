import FWCore.ParameterSet.Config as cms

def Timestamp(*args, **kwargs):
  mod = cms.EDAnalyzer('Timestamp',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
