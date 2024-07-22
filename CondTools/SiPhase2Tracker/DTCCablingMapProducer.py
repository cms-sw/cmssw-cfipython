import FWCore.ParameterSet.Config as cms

def DTCCablingMapProducer(**kwargs):
  mod = cms.EDAnalyzer('DTCCablingMapProducer',
    dummy_fill_mode = cms.string('DUMMY_FILL_DISABLED'),
    verbosity = cms.int32(0),
    csvFormat_ncolumns = cms.uint32(15),
    csvFormat_idetid = cms.uint32(0),
    csvFormat_idtcid = cms.uint32(0),
    csvFormat_igbtlinkid = cms.uint32(0),
    csvFormat_ielinkid = cms.uint32(0),
    iovBeginTime = cms.uint64(1),
    record = cms.string('TrackerDTCCablingMapRcd'),
    modulesToDTCCablingCSVFileNames = cms.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod