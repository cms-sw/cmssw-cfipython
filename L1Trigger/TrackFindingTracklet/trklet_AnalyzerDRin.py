import FWCore.ParameterSet.Config as cms

def trklet_AnalyzerDRin(**kwargs):
  mod = cms.EDAnalyzer('trklet::AnalyzerDRin',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
