import FWCore.ParameterSet.Config as cms

rawStreamFileWriterForBU = cms.OutputModule('RawStreamFileWriterForBU',
  source = cms.InputTag('rawDataCollector'),
  numEventsPerFile = cms.uint32(100),
  frdVersion = cms.uint32(6),
  microSleep = cms.int32(0),
  frdFileVersion = cms.uint32(0)
)
