import FWCore.ParameterSet.Config as cms

DTCCablingMapTestProducer = cms.EDAnalyzer('DTCCablingMapTestProducer',
  iovBeginTime = cms.uint64(1),
  record = cms.string('TrackerDetToDTCELinkCablingMap')
)
