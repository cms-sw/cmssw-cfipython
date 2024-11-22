import FWCore.ParameterSet.Config as cms

def trackerTFP_AnalyzerDemonstrator(*args, **kwargs):
  mod = cms.EDAnalyzer('trackerTFP::AnalyzerDemonstrator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
