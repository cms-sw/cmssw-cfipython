import FWCore.ParameterSet.Config as cms

def CandViewHistoAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CandViewHistoAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
