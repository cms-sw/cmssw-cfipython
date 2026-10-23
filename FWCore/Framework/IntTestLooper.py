import FWCore.ParameterSet.Config as cms

def IntTestLooper(*args, **kwargs):
  mod = cms.Looper('IntTestLooper',
    srcBeginRun = cms.untracked.VInputTag(),
    srcBeginLumi = cms.untracked.VInputTag(),
    srcEvent = cms.untracked.VInputTag(),
    srcEndLumi = cms.untracked.VInputTag(),
    srcEndRun = cms.untracked.VInputTag(),
    expectBeginRunValues = cms.untracked.vint32(),
    expectBeginLumiValues = cms.untracked.vint32(),
    expectEventValues = cms.untracked.vint32(),
    expectEndLumiValues = cms.untracked.vint32(),
    expectEndRunValues = cms.untracked.vint32(),
    expectESValue = cms.required.untracked.int32,
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
