import FWCore.ParameterSet.Config as cms

def CaloTowersExample(*args, **kwargs):
  mod = cms.EDAnalyzer('CaloTowersExample',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
