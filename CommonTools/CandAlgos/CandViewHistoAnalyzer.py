import FWCore.ParameterSet.Config as cms

def CandViewHistoAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CandViewHistoAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
