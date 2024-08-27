import FWCore.ParameterSet.Config as cms

def FWLiteESRecordWriterAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('FWLiteESRecordWriterAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
