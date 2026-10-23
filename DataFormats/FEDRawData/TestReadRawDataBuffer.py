import FWCore.ParameterSet.Config as cms

def TestReadRawDataBuffer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestReadRawDataBuffer',
    dataPattern1 = cms.required.vuint32,
    dataPattern2 = cms.required.vuint32,
    rawDataBufferTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
