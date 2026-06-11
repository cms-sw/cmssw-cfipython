import FWCore.ParameterSet.Config as cms

def DumpRawDataBuffer(*args, **kwargs):
  mod = cms.EDAnalyzer('DumpRawDataBuffer',
    minSLinkID = cms.uint32(0),
    maxSLinkID = cms.uint32(99999),
    rawDataBufferTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
