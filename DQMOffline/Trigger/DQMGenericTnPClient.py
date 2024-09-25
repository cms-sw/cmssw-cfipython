import FWCore.ParameterSet.Config as cms

def DQMGenericTnPClient(*args, **kwargs):
  mod = cms.EDAnalyzer('DQMGenericTnPClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
