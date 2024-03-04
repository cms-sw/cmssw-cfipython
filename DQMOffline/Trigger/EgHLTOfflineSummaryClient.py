import FWCore.ParameterSet.Config as cms

def EgHLTOfflineSummaryClient(**kwargs):
  mod = cms.EDAnalyzer('EgHLTOfflineSummaryClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
