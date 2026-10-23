import FWCore.ParameterSet.Config as cms

def CandHistoAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CandHistoAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
