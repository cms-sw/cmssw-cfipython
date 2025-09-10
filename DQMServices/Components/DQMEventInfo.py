import FWCore.ParameterSet.Config as cms

def DQMEventInfo(*args, **kwargs):
  mod = cms.EDProducer('DQMEventInfo',
    showHLTGlobalTag = cms.untracked.bool(False),
    eventInfoFolder = cms.untracked.string('EventInfo'),
    subSystemFolder = cms.untracked.string('YourSubsystem'),
    eventRateWindow = cms.untracked.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
