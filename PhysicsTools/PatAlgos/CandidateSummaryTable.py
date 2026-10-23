import FWCore.ParameterSet.Config as cms

def CandidateSummaryTable(*args, **kwargs):
  mod = cms.EDAnalyzer('CandidateSummaryTable',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
