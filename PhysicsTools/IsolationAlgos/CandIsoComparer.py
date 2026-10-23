import FWCore.ParameterSet.Config as cms

def CandIsoComparer(*args, **kwargs):
  mod = cms.EDAnalyzer('CandIsoComparer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
