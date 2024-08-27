import FWCore.ParameterSet.Config as cms

def OffsetAnalyzerDQM(**kwargs):
  mod = cms.EDProducer('OffsetAnalyzerDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
