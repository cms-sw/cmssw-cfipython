import FWCore.ParameterSet.Config as cms

def FWLiteESRecordWriterAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('FWLiteESRecordWriterAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
