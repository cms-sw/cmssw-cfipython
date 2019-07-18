import FWCore.ParameterSet.Config as cms

GEMDQMStatusDigi = cms.EDProducer('GEMDQMStatusDigi',
  VFATInputLabel = cms.InputTag('muonGEMDigis', 'vfatStatus'),
  GEBInputLabel = cms.InputTag('muonGEMDigis', 'gebStatus'),
  AMCInputLabel = cms.InputTag('muonGEMDigis', 'AMCStatus'),
  mightGet = cms.optional.untracked.vstring
)
