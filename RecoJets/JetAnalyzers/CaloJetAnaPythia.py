import FWCore.ParameterSet.Config as cms

def CaloJetAnaPythia(*args, **kwargs):
  mod = cms.EDAnalyzer('CaloJetAnaPythia',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
