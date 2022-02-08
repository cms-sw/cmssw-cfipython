import FWCore.ParameterSet.Config as cms

tcdsRawToDigi = cms.EDProducer('TcdsRawToDigi',
  InputLabel = cms.InputTag('rawDataCollector'),
  mightGet = cms.optional.untracked.vstring
)
