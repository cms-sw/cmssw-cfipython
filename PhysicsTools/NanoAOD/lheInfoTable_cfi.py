import FWCore.ParameterSet.Config as cms

lheInfoTable = cms.EDProducer('LHETablesProducer',
  lheInfo = cms.InputTag('externalLHEProducer')
)
