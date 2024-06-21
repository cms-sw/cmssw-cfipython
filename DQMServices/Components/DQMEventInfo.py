import FWCore.ParameterSet.Config as cms

def DQMEventInfo(**kwargs):
  mod = cms.EDProducer('DQMEventInfo',
    showHLTGlobalTag = cms.untracked.bool(False),
    eventInfoFolder = cms.untracked.string('EventInfo'),
    subSystemFolder = cms.untracked.string('YourSubsystem'),
    eventRateWindow = cms.untracked.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
