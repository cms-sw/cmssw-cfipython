import FWCore.ParameterSet.Config as cms

getEventSetupData = cms.EDAnalyzer('EventSetupRecordDataGetter',
  verbose = cms.untracked.bool(False),
  toGet = cms.VPSet(
  )
)
