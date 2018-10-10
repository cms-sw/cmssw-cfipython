import FWCore.ParameterSet.Config as cms

psMonitoring = cms.EDAnalyzer('PSMonitor',
  ugtBXInputTag = cms.InputTag('hltGtStage2Digis'),
  FolderName = cms.string('HLT/PSMonitoring'),
  histoPSet = cms.PSet(
    psColumnPSet = cms.PSet(
      nbins = cms.int32(8)
    ),
    lsPSet = cms.PSet(
      nbins = cms.int32(2500)
    )
  )
)
