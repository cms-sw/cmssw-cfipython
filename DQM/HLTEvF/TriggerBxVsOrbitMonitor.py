import FWCore.ParameterSet.Config as cms

def TriggerBxVsOrbitMonitor(*args, **kwargs):
  mod = cms.EDProducer('TriggerBxVsOrbitMonitor',
    l1tResults = cms.untracked.InputTag('gtStage2Digis'),
    hltResults = cms.untracked.InputTag('TriggerResults'),
    dqmPath = cms.untracked.string('HLT/TriggerBx'),
    minLS = cms.untracked.int32(134),
    maxLS = cms.untracked.int32(136),
    minBX = cms.untracked.int32(894),
    maxBX = cms.untracked.int32(912),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
