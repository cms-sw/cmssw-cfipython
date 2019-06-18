import FWCore.ParameterSet.Config as cms

GEMDQMSourceDigi = cms.EDProducer('GEMDQMSourceDigi',
  digisInputLabel = cms.InputTag('muonGEMDigis'),
  mightGet = cms.optional.untracked.vstring
)
