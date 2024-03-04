import FWCore.ParameterSet.Config as cms

def CandHistoAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CandHistoAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
