import FWCore.ParameterSet.Config as cms

def trackerTFP_AnalyzerMHT(*args, **kwargs):
  mod = cms.EDAnalyzer('trackerTFP::AnalyzerMHT',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
