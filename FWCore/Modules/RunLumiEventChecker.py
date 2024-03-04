import FWCore.ParameterSet.Config as cms

def RunLumiEventChecker(**kwargs):
  mod = cms.EDAnalyzer('RunLumiEventChecker',
    eventSequence = cms.required.untracked.VEventID,
    unorderedEvents = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
