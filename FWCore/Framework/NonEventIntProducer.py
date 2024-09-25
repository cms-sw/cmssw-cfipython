import FWCore.ParameterSet.Config as cms

def NonEventIntProducer(*args, **kwargs):
  mod = cms.EDProducer('NonEventIntProducer',
    ivalue = cms.int32(0),
    sleepTime = cms.uint32(0),
    consumesBeginProcessBlock = cms.InputTag(''),
    expectBeginProcessBlock = cms.untracked.int32(0),
    consumesEndProcessBlock = cms.InputTag(''),
    expectEndProcessBlock = cms.untracked.int32(0),
    consumesAccessInputProcessBlock = cms.InputTag(''),
    expectAccessInputProcessBlock = cms.untracked.int32(0),
    consumesBeginRun = cms.InputTag(''),
    expectBeginRun = cms.untracked.int32(0),
    consumesEndRun = cms.InputTag(''),
    expectEndRun = cms.untracked.int32(0),
    consumesBeginLuminosityBlock = cms.InputTag(''),
    expectBeginLuminosityBlock = cms.untracked.int32(0),
    consumesEndLuminosityBlock = cms.InputTag(''),
    expectEndLuminosityBlock = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
