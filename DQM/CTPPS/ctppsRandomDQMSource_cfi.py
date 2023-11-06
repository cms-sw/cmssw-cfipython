import FWCore.ParameterSet.Config as cms

ctppsRandomDQMSource = cms.EDProducer('CTPPSRandomDQMSource',
  tagRPixDigi = cms.InputTag('ctppsPixelDigisAlCaRecoProducer'),
  folderName = cms.untracked.string('PPSRANDOM/RandomPixel'),
  RPStatusWord = cms.untracked.uint32(32776),
  mightGet = cms.optional.untracked.vstring
)
