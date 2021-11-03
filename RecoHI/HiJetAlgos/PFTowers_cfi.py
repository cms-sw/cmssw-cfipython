import FWCore.ParameterSet.Config as cms

PFTowers = cms.EDProducer('PFTowers',
  useHF = cms.bool(True),
  src = cms.InputTag('particleFlow'),
  mightGet = cms.optional.untracked.vstring
)
