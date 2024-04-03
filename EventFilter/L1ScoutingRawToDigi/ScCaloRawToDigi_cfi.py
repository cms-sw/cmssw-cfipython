import FWCore.ParameterSet.Config as cms

ScCaloRawToDigi = cms.EDProducer('ScCaloRawToDigi',
  srcInputTag = cms.InputTag('rawDataCollector'),
  dataSource = cms.PSet(
    dataSourceMode = cms.string('TCP'),
    jetSourceIdList = cms.vint32(22),
    eGammaSourceIdList = cms.vint32(23),
    tauSourceIdList = cms.vint32(25),
    etSumSourceIdList = cms.vint32(24),
    dmaSourceId = cms.int32(2)
  ),
  enableAllSums = cms.bool(True),
  debug = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
