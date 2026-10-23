import FWCore.ParameterSet.Config as cms

def EventIDChecker(*args, **kwargs):
  mod = cms.EDAnalyzer('EventIDChecker',
    eventSequence = cms.required.untracked.VEventID,
    multiProcessSequentialEvents = cms.untracked.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
