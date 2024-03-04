import FWCore.ParameterSet.Config as cms

def trackerTFP_AnalyzerKFin(**kwargs):
  mod = cms.EDAnalyzer('trackerTFP::AnalyzerKFin',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
