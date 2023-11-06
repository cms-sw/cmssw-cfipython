import FWCore.ParameterSet.Config as cms

source = cms.Source('SourceWithWaits',
  timePerLumi = cms.required.untracked.uint32,
  eventsPerLumi = cms.required.untracked.vuint32,
  lumisPerRun = cms.required.untracked.uint32
)
