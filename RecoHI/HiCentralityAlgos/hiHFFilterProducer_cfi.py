import FWCore.ParameterSet.Config as cms

hiHFFilterProducer = cms.EDProducer('HiHFFilterProducer',
  srcTowers = cms.InputTag('towerMaker'),
  mightGet = cms.optional.untracked.vstring
)
