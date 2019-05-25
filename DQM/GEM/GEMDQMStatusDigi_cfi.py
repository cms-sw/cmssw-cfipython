import FWCore.ParameterSet.Config as cms

GEMDQMStatusDigi = cms.EDProducer('GEMDQMStatusDigi',
  VFATInputLabel = cms.InputTag('muonGEMDigis', 'vfatStatus'),
  GEBInputLabel = cms.InputTag('muonGEMDigis', 'GEBStatus'),
  AMCInputLabel = cms.InputTag('muonGEMDigis', 'AMCStatus')
)
