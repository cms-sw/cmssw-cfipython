import FWCore.ParameterSet.Config as cms

def RunLumiEventChecker(**kwargs):
  mod = cms.EDAnalyzer('RunLumiEventChecker',
    eventSequence = cms.required.untracked.VEventID,
    minNumberOfEvents = cms.untracked.uint32(0),
    maxNumberOfEvents = cms.untracked.uint32(0),
    unorderedEvents = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
