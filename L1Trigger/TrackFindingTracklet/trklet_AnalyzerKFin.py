import FWCore.ParameterSet.Config as cms

def trklet_AnalyzerKFin(**kwargs):
  mod = cms.EDAnalyzer('trklet::AnalyzerKFin',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
