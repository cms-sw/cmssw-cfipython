import FWCore.ParameterSet.Config as cms

tkInstLumiTable = cms.EDProducer('TkInstLumiTableProducer',
  name = cms.string(''),
  doc = cms.string(''),
  extension = cms.bool(False),
  lumiScalers = cms.InputTag('scalersRawToDigi'),
  metadata = cms.InputTag('onlineMetaDataDigis'),
  mightGet = cms.optional.untracked.vstring
)
