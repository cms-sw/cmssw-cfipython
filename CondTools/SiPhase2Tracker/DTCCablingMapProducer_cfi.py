import FWCore.ParameterSet.Config as cms

DTCCablingMapProducer = cms.EDAnalyzer('DTCCablingMapProducer',
  generate_fake_valid_gbtlink_and_elinkid = cms.bool(False),
  verbosity = cms.int32(0),
  csvFormat_idetid = cms.uint32(0),
  csvFormat_ncolumns = cms.uint32(15),
  csvFormat_idtcid = cms.uint32(10),
  csvFormat_igbtlinkid = cms.uint32(11),
  csvFormat_ielinkid = cms.uint32(12),
  iovBeginTime = cms.uint64(1),
  record = cms.string('TrackerDTCCablingMapRcd'),
  modulesToDTCCablingCSVFileNames = cms.vstring()
)
