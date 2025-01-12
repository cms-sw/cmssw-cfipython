import FWCore.ParameterSet.Config as cms

def DTHFakeReader(*args, **kwargs):
  mod = cms.EDProducer('DTHFakeReader',
    fillRandom = cms.untracked.bool(False),
    meanSize = cms.untracked.uint32(1024),
    width = cms.untracked.uint32(1024),
    injectErrPpm = cms.untracked.uint32(1024),
    sourceIdList = cms.untracked.vuint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
