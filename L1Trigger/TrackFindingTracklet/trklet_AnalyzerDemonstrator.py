import FWCore.ParameterSet.Config as cms

def trklet_AnalyzerDemonstrator(**kwargs):
  mod = cms.EDAnalyzer('trklet::AnalyzerDemonstrator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
