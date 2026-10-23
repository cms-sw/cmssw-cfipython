import FWCore.ParameterSet.Config as cms

def Mixing2DB(*args, **kwargs):
  mod = cms.EDAnalyzer('Mixing2DB',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
