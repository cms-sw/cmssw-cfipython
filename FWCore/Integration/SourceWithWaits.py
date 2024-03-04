import FWCore.ParameterSet.Config as cms

def SourceWithWaits(**kwargs):
  mod = cms.Source('SourceWithWaits',
    timePerLumi = cms.required.untracked.double,
    sleepAfterStartOfRun = cms.required.untracked.double,
    eventsPerLumi = cms.required.untracked.vuint32,
    lumisPerRun = cms.required.untracked.uint32,
    multipleEntriesForRun = cms.untracked.uint32(0),
    multipleEntriesForLumi = cms.untracked.uint32(0),
    declareLast = cms.untracked.bool(False),
    declareAllLast = cms.untracked.bool(False)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
