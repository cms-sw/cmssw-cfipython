import FWCore.ParameterSet.Config as cms

def CorrectECALIsolation(*args, **kwargs):
  mod = cms.EDAnalyzer('CorrectECALIsolation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
