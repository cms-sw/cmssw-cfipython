import FWCore.ParameterSet.Config as cms

ScGMTRawToDigi = cms.EDProducer('ScGMTRawToDigi',
  srcInputTag = cms.InputTag('rawDataCollector'),
  skipInterm = cms.bool(True),
  debug = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
