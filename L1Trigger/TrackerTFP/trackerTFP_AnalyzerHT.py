import FWCore.ParameterSet.Config as cms

def trackerTFP_AnalyzerHT(*args, **kwargs):
  mod = cms.EDAnalyzer('trackerTFP::AnalyzerHT',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
