import FWCore.ParameterSet.Config as cms

def EventIDChecker(**kwargs):
  mod = cms.EDAnalyzer('EventIDChecker',
    eventSequence = cms.required.untracked.VEventID,
    multiProcessSequentialEvents = cms.untracked.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
