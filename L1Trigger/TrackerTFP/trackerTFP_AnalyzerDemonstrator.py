import FWCore.ParameterSet.Config as cms

def trackerTFP_AnalyzerDemonstrator(**kwargs):
  mod = cms.EDAnalyzer('trackerTFP::AnalyzerDemonstrator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
