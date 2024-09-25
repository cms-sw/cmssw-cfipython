import FWCore.ParameterSet.Config as cms

def trackerTFP_AnalyzerZHT(*args, **kwargs):
  mod = cms.EDAnalyzer('trackerTFP::AnalyzerZHT',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
