import FWCore.ParameterSet.Config as cms

def DQMRivetClient(*args, **kwargs):
  mod = cms.EDAnalyzer('DQMRivetClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
