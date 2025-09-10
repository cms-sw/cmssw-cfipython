import FWCore.ParameterSet.Config as cms

def trackerTFP_AnalyzerDR(*args, **kwargs):
  mod = cms.EDAnalyzer('trackerTFP::AnalyzerDR',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
